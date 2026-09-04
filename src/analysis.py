"""Analyze sample sales data and create a monthly revenue chart."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "sample_sales.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "monthly_revenue.png"


def load_sales_data(path: Path | str = DATA_PATH) -> pd.DataFrame:
    """Load sales data and calculate revenue for each transaction."""
    sales = pd.read_csv(path, parse_dates=["date"])
    required_columns = {"date", "region", "category", "units_sold", "unit_price"}
    missing_columns = required_columns - set(sales.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    sales["revenue"] = sales["units_sold"] * sales["unit_price"]
    return sales


def summarize_sales(sales: pd.DataFrame) -> dict[str, pd.Series | float]:
    """Return headline and grouped sales metrics."""
    return {
        "total_revenue": float(sales["revenue"].sum()),
        "monthly_revenue": sales.groupby(sales["date"].dt.to_period("M"))["revenue"].sum(),
        "revenue_by_category": sales.groupby("category")["revenue"].sum().sort_values(ascending=False),
        "revenue_by_region": sales.groupby("region")["revenue"].sum().sort_values(ascending=False),
    }


def plot_monthly_revenue(monthly_revenue: pd.Series, output_path: Path | str = OUTPUT_PATH) -> None:
    """Save a clear chart of monthly revenue."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(8, 4.5))
    axis.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker="o", color="#1f77b4")
    axis.set_title("Monthly Revenue")
    axis.set_xlabel("Month")
    axis.set_ylabel("Revenue (USD)")
    axis.grid(axis="y", alpha=0.3)
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


def main() -> None:
    sales = load_sales_data()
    summary = summarize_sales(sales)
    plot_monthly_revenue(summary["monthly_revenue"])

    print(f"Total revenue: ${summary['total_revenue']:,.2f}")
    print("\nRevenue by category:")
    print(summary["revenue_by_category"])
    print("\nRevenue by region:")
    print(summary["revenue_by_region"])
    print(f"\nChart saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
