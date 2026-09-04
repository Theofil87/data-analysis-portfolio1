# Python Data Analysis Portfolio

A small, reproducible data-analysis project that explores monthly sales performance by product category and region. It is designed as a clean starting point for a professional portfolio.

## Project structure

```text
.
├── data/               # Source data (sample data included)
├── notebooks/          # Exploratory notebooks
├── src/                # Reusable analysis code
└── tests/              # Automated checks
```

## Getting started

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis:

   ```bash
   python -m src.analysis
   ```

The command writes a chart to `outputs/monthly_revenue.png` and prints summary metrics. Run checks with `pytest`.

## Example questions answered

- How does total revenue change month to month?
- Which product category produces the most revenue?
- Which region contributes the most sales?

## Data

`data/sample_sales.csv` is synthetic data created solely for this example. Replace it with your own documented dataset when adapting the project.
