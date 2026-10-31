# 🍽️ Restaurant Sales Analysis & Demand Forecasting

Hi, I'm **Riham Hussain**, an AI & Data Science Enthusiast! 👋

An interactive restaurant analytics dashboard built using **Python, Streamlit, Prophet, and MLxtend**.

This project provides restaurant business insights through sales analysis, menu profitability evaluation, market basket analysis, and 30-day revenue forecasting.

## 📌 Features

### 1. KPI Summary Dashboard
Tracks important business performance indicators:
- Total Revenue
- Total Profit
- Total Orders
- Average Order Value (AOV)

### 2. Sales Performance & Peak Hours
Interactive Plotly visualizations to analyze:
- Revenue by Hour of Day
- Revenue by Day of Week
- Peak operating hours
- Daily sales performance

### 3. Menu Engineering – BCG Matrix

Categorizes menu items into four strategic categories based on sales volume and average profit:

| Category | Business Strategy |
|---|---|
| ⭐ Star | Keep & Feature |
| 🐴 Plowhorse | Increase Price |
| 🧩 Puzzle | Promote / Rebrand |
| 🐶 Dog | Remove / Revamp |

The matrix uses sales volume and average profit to help identify high-performing and underperforming menu items.

### 4. Market Basket Analysis – Apriori Algorithm

Uses the Apriori algorithm to identify menu items frequently purchased together.

The analysis calculates:
- **Support:** Frequency of item combinations.
- **Confidence:** Likelihood of purchasing another item.
- **Lift:** Strength of association between items.

Business applications:
- Combo meal recommendations.
- Cross-selling opportunities.
- Upselling strategies.
- Menu bundling and pricing decisions.

### 5. 30-Day Sales Forecasting

Uses Meta's Prophet time-series forecasting model to predict daily restaurant revenue for the next 30 days.

Features include:
- Historical revenue trends.
- Yearly seasonality.
- Weekly seasonality.
- Predicted daily revenue.
- Upper and lower forecast confidence intervals.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations and synthetic data generation |
| Plotly Express | Interactive charts |
| Plotly Graph Objects | Forecast visualization |
| Prophet | Time-series forecasting |
| MLxtend | Apriori algorithm and association rules |

## 📂 Project Structure

```text
restaurant_sales_forecasting/
│
├── app.py
├── generate_data.py
├── restaurant_sales.csv
├── requirements.txt
├── LICENSE
└── README.md
```

## 📊 Dataset Overview

The project uses a synthetic restaurant transaction dataset generated using `generate_data.py`.

The dataset contains approximately 5,000 generated orders across one year, with individual item-level transaction records.

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `timestamp` | Order date and time |
| `item_name` | Name of the menu item |
| `category` | Menu category |
| `quantity` | Quantity ordered |
| `cost_price` | Cost price per item |
| `selling_price` | Selling price per item |
| `order_type` | Dine-In, Takeout, or Delivery |

### Menu Categories

- Mains
- Starters
- Beverages
- Desserts

The dataset includes randomly generated transactions, menu prices, quantities, and order types.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/restaurant_sales_forecasting
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Create a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Running the Project

### Step 1: Generate the Dataset (Optional)

If you want to regenerate the synthetic restaurant transaction data:

```bash
python generate_data.py
```

This creates:

```text
restaurant_sales.csv
```

**Note:** The application expects `restaurant_sales.csv` in the project root. Generate it before launching the application if the dataset is not already present.

### Step 2: Launch the Streamlit Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

### Step 3: Explore the Dashboard

Use the sidebar filters to select:
- Order Type
- Category

Explore the four dashboard sections:

1. Sales & Peak Hours
2. Menu Engineering
3. Basket Analysis
4. Prophet Forecasting

## 🎯 Key Learning Outcomes

- Building interactive dashboards with Streamlit.
- Performing exploratory data analysis.
- Calculating business KPIs using Pandas.
- Analyzing restaurant sales and profitability.
- Applying the BCG menu engineering matrix.
- Implementing market basket analysis using Apriori.
- Understanding support, confidence, and lift.
- Performing time-series forecasting using Prophet.
- Creating interactive visualizations with Plotly.

## ⚠️ Limitations

- The dataset is synthetic and does not represent actual restaurant transactions.
- Sales forecasts are based on generated historical data.
- Association rules depend on the available transaction combinations and selected filters.
- Forecast accuracy should be evaluated using real historical sales data before business deployment.

## 📜 License

This project is distributed under the **MIT License**. See the `LICENSE` file for details.

## 👩‍💻 Author

**Riham Hussain**

AI & Data Science Enthusiast

GitHub: [Riham203](https://github.com/Riham203)
