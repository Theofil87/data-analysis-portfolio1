from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from src.analysis import (
    load_sales_data,
    plot_monthly_revenue,
    plot_revenue_by_category,
    plot_revenue_by_region,
    summarize_sales,
)

def test_load_sales_data_calculates_revenue():
    sales = load_sales_data()

    assert "revenue" in sales.columns
    assert sales.loc[0, "revenue"] == 2160
    assert pd.api.types.is_datetime64_any_dtype(sales["date"])


def test_summary_contains_expected_total():
    summary = summarize_sales(load_sales_data())

    assert summary["total_revenue"] == 16554.0
    assert len(summary["monthly_revenue"]) == 3


def test_plot_monthly_revenue_creates_file(tmp_path: Path):
    summary = summarize_sales(load_sales_data())
    chart_path = tmp_path / "monthly_revenue.png"

    plot_monthly_revenue(summary["monthly_revenue"], chart_path)

    assert chart_path.exists()
    assert chart_path.stat().st_size > 0


def test_plot_revenue_by_category_creates_file(tmp_path: Path):
    summary = summarize_sales(load_sales_data())
    chart_path = tmp_path / "revenue_by_category.png"

    plot_revenue_by_category(
        summary["revenue_by_category"],
        chart_path,
    )

    assert chart_path.exists()
    assert chart_path.stat().st_size > 0


def test_plot_revenue_by_region_creates_file(tmp_path: Path):
    summary = summarize_sales(load_sales_data())
    chart_path = tmp_path / "revenue_by_region.png"

    plot_revenue_by_region(
        summary["revenue_by_region"],
        chart_path,
    )

    assert chart_path.exists()
    assert chart_path.stat().st_size > 0
