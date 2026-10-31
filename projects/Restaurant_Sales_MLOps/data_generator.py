import numpy as np
import pandas as pd


def generate_restaurant_data(days: int = 730) -> pd.DataFrame:
    """Generates synthetic daily sales data for a restaurant."""
    np.random.seed(42)
    date_range = pd.date_range(end=pd.Timestamp.now(), periods=days, freq="D")

    base_sales = 1500
    df = pd.DataFrame({"date": date_range})

    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["is_weekend"] = df["day_of_week"].isin([4, 5, 6]).astype(int)

    # Seasonal & Trend multipliers
    weekend_boost = df["is_weekend"] * 600
    seasonal_boost = np.sin(df["month"] * (2 * np.pi / 12)) * 300
    promotions = np.random.choice([0, 1], size=days, p=[0.8, 0.2]) * 400
    noise = np.random.normal(0, 150, size=days)

    df["promotion"] = promotions
    df["seating_capacity"] = 120
    df["average_order_value"] = np.random.uniform(22.0, 35.0, size=days)
    df["daily_sales"] = (
        base_sales + weekend_boost + seasonal_boost + promotions + noise
    ).round(2)

    return df


if __name__ == "__main__":
    df = generate_restaurant_data()
    df.to_csv("restaurant_sales.csv", index=False)
    print("✅ Successfully generated 'restaurant_sales.csv'")