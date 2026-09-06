"""Analyze sample sales data and create revenue visualizations."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "sample_sales.csv"

MONTHLY_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "monthly_revenue.png"
CATEGORY_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "revenue_by_category.png"
REGION_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "revenue_by_region.png"


def load_sales_data(path: Path | str = DATA_PATH) -> pd.DataFrame:
    """Load sales data and calculate revenue for each transaction."""
    sales = pd.read_csv(path, parse_dates=["date"])

    required_columns = {
        "date",
        "region",
        "category",
        "units_sold",
        "unit_price",
    }

    missing_columns = required_columns - set(sales.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    sales["revenue"] = sales["units_sold"] * sales["unit_price"]

    return sales


def summarize_sales(sales: pd.DataFrame) -> dict[str, pd.Series | float]:
    """Return headline and grouped sales metrics."""
    return {
        "total_revenue": float(sales["revenue"].sum()),
        "monthly_revenue": (
            sales.groupby(sales["date"].dt.to_period("M"))["revenue"].sum()
        ),
        "revenue_by_category": (
            sales.groupby("category")["revenue"]
            .sum()
            .sort_values(ascending=False)
        ),
        "revenue_by_region": (
            sales.groupby("region")["revenue"]
            .sum()
            .sort_values(ascending=False)
        ),
    }


def plot_monthly_revenue(
    monthly_revenue: pd.Series,
    output_path: Path | str = MONTHLY_OUTPUT_PATH,
) -> None:
    """Save a line chart of monthly revenue."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(8, 4.5))

    axis.plot(
        monthly_revenue.index.astype(str),
        monthly_revenue.values,
        marker="o",
    )

    axis.set_title("Monthly Revenue")
    axis.set_xlabel("Month")
    axis.set_ylabel("Revenue (USD)")
    axis.grid(axis="y", alpha=0.3)

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)

    plt.close(figure)


def plot_revenue_by_category(
    revenue_by_category: pd.Series,
    output_path: Path | str = CATEGORY_OUTPUT_PATH,
) -> None:
    """Save a bar chart of revenue by product category."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(8, 4.5))

    axis.bar(
        revenue_by_category.index,
        revenue_by_category.values,
    )

    axis.set_title("Revenue by Category")
    axis.set_xlabel("Category")
    axis.set_ylabel("Revenue (USD)")
    axis.tick_params(axis="x", rotation=45)
    axis.grid(axis="y", alpha=0.3)

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)

    plt.close(figure)


def plot_revenue_by_region(
    revenue_by_region: pd.Series,
    output_path: Path | str = REGION_OUTPUT_PATH,
) -> None:
    """Save a bar chart of revenue by region."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(8, 4.5))

    axis.bar(
        revenue_by_region.index,
        revenue_by_region.values,
    )

    axis.set_title("Revenue by Region")
    axis.set_xlabel("Region")
    axis.set_ylabel("Revenue (USD)")
    axis.tick_params(axis="x", rotation=45)
    axis.grid(axis="y", alpha=0.3)

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)

    plt.close(figure)


def main() -> None:
    """Run the sales analysis and create all visualizations."""
    sales = load_sales_data()
    summary = summarize_sales(sales)

    plot_monthly_revenue(summary["monthly_revenue"])
    plot_revenue_by_category(summary["revenue_by_category"])
    plot_revenue_by_region(summary["revenue_by_region"])

    print(f"Total revenue: ${summary['total_revenue']:,.2f}")

    print("\nRevenue by category:")
    print(summary["revenue_by_category"])

    print("\nRevenue by region:")
    print(summary["revenue_by_region"])

    print("\nCharts saved to:")
    print(f"- {MONTHLY_OUTPUT_PATH}")
    print(f"- {CATEGORY_OUTPUT_PATH}")
    print(f"- {REGION_OUTPUT_PATH}")


if __name__ == "__main__":
    main()