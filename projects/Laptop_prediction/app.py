import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Page Configuration
st.set_page_config(
    page_title="Laptop Price Predictor & AI Advisor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 1. SESSION STATE (AUTHENTICATION & CHAT HISTORY)
# -----------------------------------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I am your AI Laptop Advisor. Ask me anything about laptop specs, performance, or pricing!"}
    ]

# -----------------------------------------------------------------------------
# 2. DATASET GENERATION & MODEL TRAINING
# -----------------------------------------------------------------------------
@st.cache_data
def load_datasets_and_models():
    np.random.seed(42)
    n = 300

    # New Laptop Dataset
    new_df = pd.DataFrame({
        'RAM_GB': np.random.choice([8, 16, 32], n),
        'Storage_GB': np.random.choice([256, 512, 1024], n),
        'Screen_Size': np.random.choice([13.3, 14.0, 15.6, 17.3], n)
    })
    new_df['Price_USD'] = (new_df['RAM_GB'] * 45) + (new_df['Storage_GB'] * 0.6) + (new_df['Screen_Size'] * 20) + np.random.normal(200, 40, n)

    # Old/Used Laptop Dataset (incorporating age factor)
    old_df = new_df.copy()
    old_df['Age_Years'] = np.random.randint(1, 6, n)
    old_df['Price_USD'] = old_df['Price_USD'] * (1 - (old_df['Age_Years'] * 0.12))

    # Train Linear Regression Models
    model_new = LinearRegression()
    model_new.fit(new_df[['RAM_GB', 'Storage_GB', 'Screen_Size']], new_df['Price_USD'])

    model_old = LinearRegression()
    model_old.fit(old_df[['RAM_GB', 'Storage_GB', 'Screen_Size', 'Age_Years']], old_df['Price_USD'])

    return new_df, old_df, model_new, model_old

new_df, old_df, model_new, model_old = load_datasets_and_models()

# -----------------------------------------------------------------------------
# 3. LOGIN PAGE
# -----------------------------------------------------------------------------
def render_login_page():
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80",
            caption="Smart Valuation Platform",
            use_container_width=True
        )

    with col2:
        st.title("🔑 Portal Access")
        st.caption("Sign in to access valuations, ML predictions, and AI recommendations.")

        username_input = st.text_input("Username", key="login_username")
        password_input = st.text_input("Password", type="password", key="login_password")

        if st.button("Sign In", type="primary", use_container_width=True):
            if username_input and password_input:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username_input
                st.rerun()
            else:
                st.error("Please enter both username and password.")

# -----------------------------------------------------------------------------
# 4. MAIN DASHBOARD & NAVIGATION
# -----------------------------------------------------------------------------
def render_main_app():
    # Sidebar Setup
    with st.sidebar:
        st.title("💻 Laptop Portal")
        st.markdown(f"User: **{st.session_state['username']}**")
        st.divider()

        menu = st.radio(
            "Navigation Menu",
            ["🏠 Home", "📊 Price Predictor", "🤖 AI Chatbot"],
            index=0
        )

        st.divider()
        if st.button("Log Out", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["username"] = ""
            st.rerun()

    # SECTION 1: HOME PAGE
    if menu == "🏠 Home":
        st.title(" Welcome to Laptop Valuer AI")
        st.write("An intelligent analytics engine built to estimate laptop values and guide purchasing decisions.")

        st.image(
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1200&q=80",
            use_container_width=True
        )

        st.subheader("Features Available:")
        st.markdown("""
        * **Old & New Laptop Datasets:** Dual data pipelines tailored to pristine vs. depreciating used inventory.
        * **Linear Regression Engine:** Machine Learning prediction based on RAM, SSD storage, display dimensions, and hardware age.
        * **Interactive Sliders:** Live recalculations without mandatory form submit lockouts.
        * **AI Advisory Chatbot:** Get instant spec recommendations and tech advice.
        """)

    # SECTION 2: PRICE PREDICTOR PAGE
    elif menu == "📊 Price Predictor":
        st.title("📊 Laptop Price Predictor")
        st.caption("Trained via Scikit-Learn Linear Regression")

        category = st.radio(
            "Select Laptop Condition:",
            ["New Laptop", "Old/Used Laptop"],
            horizontal=True
        )

        st.subheader("Configure Specifications")
        col_a, col_b = st.columns(2)

        # Sliders placed directly outside of st.form for live responsiveness
        with col_a:
            ram = st.select_slider(
                "RAM (GB)",
                options=[8, 16, 32],
                value=16,
                key="ram_input"
            )
            storage = st.select_slider(
                "Storage (GB SSD)",
                options=[256, 512, 1024],
                value=512,
                key="storage_input"
            )

        with col_b:
            screen_size = st.selectbox(
                "Screen Size (Inches)",
                options=[13.3, 14.0, 15.6, 17.3],
                index=2,
                key="screen_input"
            )
            if category == "Old/Used Laptop":
                age = st.slider(
                    "Laptop Age (Years)",
                    min_value=1,
                    max_value=5,
                    value=2,
                    key="age_input"
                )
            else:
                age = 0

        st.divider()

        # Perform Live Linear Regression Prediction
        if category == "New Laptop":
            input_df = pd.DataFrame([[ram, storage, screen_size]], columns=['RAM_GB', 'Storage_GB', 'Screen_Size'])
            predicted_price = model_new.predict(input_df)[0]
        else:
            input_df = pd.DataFrame([[ram, storage, screen_size, age]], columns=['RAM_GB', 'Storage_GB', 'Screen_Size', 'Age_Years'])
            predicted_price = model_old.predict(input_df)[0]

        st.metric(
            label=f"Estimated Valuation ({category})",
            value=f"${max(100, int(predicted_price)):,}"
        )

    # SECTION 3: AI CHATBOT PAGE
    elif menu == "🤖 AI Chatbot":
        st.title("🤖 AI Laptop Advisor")
        st.caption("Ask questions regarding specs, buying advice, or old vs. new tradeoffs.")

        # Render Previous Messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input Handler
        if prompt := st.chat_input("Ask a question (e.g., 'Should I get 16GB RAM for video editing?')..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Rule-Based Assistant Responses
            prompt_lower = prompt.lower()
            if "ram" in prompt_lower:
                bot_response = "8GB RAM is fine for general web browsing, but 16GB is the sweet spot for modern multi-tasking, coding, and casual gaming."
            elif "old" in prompt_lower or "used" in prompt_lower:
                bot_response = "When purchasing a used laptop, check battery wear levels, inspect the screen for dead pixels, and ensure thermal fans aren't clogged."
            elif "storage" in prompt_lower or "ssd" in prompt_lower:
                bot_response = "Always opt for an SSD over a traditional HDD. 512GB SSD is standard, but if you store large media files, consider 1TB."
            else:
                bot_response = "Focus on prioritizing your CPU and RAM first, as storage can easily be expanded externally later."

            with st.chat_message("assistant"):
                st.markdown(bot_response)

            st.session_state.messages.append({"role": "assistant", "content": bot_response})

# -----------------------------------------------------------------------------
# 5. APP EXECUTION CONTROL
# -----------------------------------------------------------------------------
if not st.session_state["authenticated"]:
    render_login_page()
else:
    render_main_app()