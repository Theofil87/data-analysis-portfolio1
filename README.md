# 📊 Sales Data Dashboard

An interactive Streamlit dashboard for exploring sales data with KPIs and visualizations. Built with Python, Pandas and Plotly — ideal for demonstrating data analysis and dashboarding skills.

[Live Demo](https://theofi187-data-analysis.streamlit.app) • ![Interactive Streamlit Dashboard](images/dashboard.png)

<!-- Optional badges (enable CI / coverage in your repo and replace URLs) -->
<!--
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Build Status](https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg)](https://github.com/<owner>/<repo>/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](/LICENSE)
-->

## Table of contents
- [Features](#features)
- [Technologies](#technologies)
- [Demo](#demo)
- [Quick start](#quick-start)
- [Usage](#usage)
- [Project structure](#project-structure)
- [Data](#data)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Interactive region filtering
- Total Revenue, Total Transactions, Average Transaction Value KPIs
- Monthly Revenue visualization (time series)
- Interactive sales data exploration with filters and drill-downs

## Technologies
- Python
- Pandas
- Streamlit
- Plotly
- Git / GitHub

## Demo
Try the live demo here: https://theofi187-data-analysis.streamlit.app

## Quick start

1. Clone the repo
   ```bash
   git clone https://github.com/Theofil87/data-analysis-portfolio1.git
   cd data-analysis-portfolio1
   ```

2. Create a virtual environment and install requirements
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

   If you use pip-tools / poetry / pyproject.toml, add instructions here accordingly.

3. Run the Streamlit app locally
   ```bash
   streamlit run app.py
   ```

4. Open http://localhost:8501 in your browser.

## Usage
- Use the region filter to focus on specific markets.
- Hover or click interactive Plotly charts for details.
- Adjust date range and groupings in the controls (if implemented in UI).

(If you’d like, add a short GIF or an extra screenshot showing an interactive filter being used.)

## Project structure
```text
data-analysis-portfolio/
│
├── app.py                 # Streamlit dashboard application (entry point)
├── src/
│   ├── analysis.py        # Data analysis functions
│   └── generate_data.py   # Sample data generation
│
├── data/                  # Datasets (CSV or other)
├── images/                # Screenshots and assets used in README
├── notebooks/             # Exploratory analysis notebooks
├── tests/                 # Automated tests
├── requirements.txt       # Project dependencies
├── pyproject.toml         # Project configuration (optional)
└── README.md
```

## Data
- The `data/` folder contains sample dataset(s) used by the app.
- If data is large or private, provide a small sample CSV and code to regenerate synthetic data (`src/generate_data.py`).

## Tests
- Run tests with:
  ```bash
  pytest
  ```
- Add CI (GitHub Actions) to run tests automatically and add a build badge.

## Contributing
Contributions are welcome! Suggested steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and add tests
4. Open a pull request describing the change

Add a CONTRIBUTING.md if you want a detailed contributor guide.

## License
Add a LICENSE file (for example, MIT). If you want, I can add a standard MIT license file to the repo.

## Contact
Maintainer: Theofil87 — link to your GitHub profile: https://github.com/Theofil87
