<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&pause=1000&color=F5A623&center=true&vCenter=true&width=700&lines=🥇+Gold+Price+Prediction;AI-Powered+Market+Forecasting;KNN+Regression+%7C+R²+≈+99.8%25" alt="Typing SVG" />

<br/>

<p align="center">
  <strong>Predict the GLD (Gold ETF) closing price in real time - powered by Machine Learning</strong><br/>
  <sub>11 global market indicators &nbsp;·&nbsp; 7 years of daily trading data &nbsp;·&nbsp; R² ≈ 99.8%</sub>
</p>

<br/>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.23%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F5A623?style=for-the-badge)](LICENSE)

<br/>

[![GitHub stars](https://img.shields.io/github/stars/anubhab1601/Gold_Price_Prediction?style=social)](https://github.com/anubhab1601/Gold_Price_Prediction/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/anubhab1601/Gold_Price_Prediction?style=social)](https://github.com/anubhab1601/Gold_Price_Prediction/network)
[![GitHub issues](https://img.shields.io/github/issues/anubhab1601/Gold_Price_Prediction)](https://github.com/anubhab1601/Gold_Price_Prediction/issues)

</div>

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🧠 How It Works](#-how-it-works)
- [📊 Model Performance](#-model-performance)
- [📁 Dataset Overview](#-dataset-overview)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Getting Started](#️-getting-started)
- [🔌 API Reference](#-api-reference)
- [📓 Notebook](#-notebook)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>🎯 Real-Time Prediction</h3>
      Enter 11 market indicators and receive an instant GLD price estimate - no page reload needed.
    </td>
    <td width="50%">
      <h3>📈 High-Accuracy Model</h3>
      KNN Regressor tuned to <code>k=2</code> via elbow-curve analysis achieves <strong>R² ≈ 0.998</strong>.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🌐 REST API</h3>
      Programmatic access via <code>POST /api/predict</code> - integrate predictions into any app.
    </td>
    <td width="50%">
      <h3>📊 Live Metrics Dashboard</h3>
      MAE, MSE, RMSE, R², dataset statistics, and date range surfaced directly in the UI.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>📱 Responsive Design</h3>
      Modern UI built with Inter typography, Font Awesome icons, and a clean gold-accented palette.
    </td>
    <td width="50%">
      <h3>📓 Full EDA Notebook</h3>
      Jupyter notebook with exploratory analysis, feature correlations, and model comparison.
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology |
|:---|:---|
| **Backend** | Python 3.8+, Flask 2.3+ |
| **ML / Data** | scikit-learn, Pandas, NumPy |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Fonts & Icons** | Google Fonts (Inter), Font Awesome 6 |
| **ML Algorithm** | K-Nearest Neighbours Regressor |
| **Deployment** | Gunicorn (production WSGI) |

---

## 🧠 How It Works

```
 Market Inputs  ──►  StandardScaler  ──►  KNN Regressor (k=2)  ──►  GLD Price
 (11 features)        (fitted on            (80/20 split,              (USD)
                       train set)            R² ≈ 0.998)
```

1. **Data** - 1,718 daily rows of global market data (Jan 2011 – Dec 2018) loaded from `FINAL_USO.csv`.
2. **Preprocessing** - Features scaled with `StandardScaler` fitted **only** on the training set to prevent data leakage.
3. **Model Selection** - Elbow-curve plotted for `k = 1` to `20`; `k = 2` minimises error without overfitting.
4. **Prediction** - User inputs are scaled with the same scaler, then passed to the trained KNN model for an instant result.

---

## 📊 Model Performance

<div align="center">

| Metric | Score |
|:---:|:---:|
| 🏆 **R² Score** | **≈ 0.9983** |
| 📉 **MAE** | ≈ $0.59 |
| 📐 **MSE** | ≈ $1.21 |
| 📏 **RMSE** | ≈ $1.10 |

</div>

> The model explains **99.83%** of variance in GLD closing prices on completely unseen test data.

---

## 📁 Dataset Overview

| Property | Detail |
|:---|:---|
| **Source file** | `Dataset/FINAL_USO.csv` |
| **Records** | 1,718 daily rows |
| **Date Range** | January 2011 – December 2018 |
| **Total Columns** | 81 |
| **Features Used** | 11 |
| **Target Column** | `Close` - GLD ETF daily closing price (USD) |
| **Missing Values** | ✅ None |
| **Duplicates** | ✅ None |

### 🔑 11 Input Features

<details>
<summary><strong>Click to expand feature descriptions</strong></summary>

<br/>

| # | Feature | Description |
|:---:|:---|:---|
| 1 | `SP_close` | S&P 500 Index - daily closing value |
| 2 | `DJ_close` | Dow Jones Industrial Average - daily close |
| 3 | `EU_Price` | EUR / USD exchange rate |
| 4 | `OF_Price` | Crude Oil Futures price (USD / barrel) |
| 5 | `SF_Price` | Silver Futures price |
| 6 | `PLT_Price` | Platinum Futures price |
| 7 | `PLD_Price` | Palladium Futures price |
| 8 | `USDI_Price` | US Dollar Index |
| 9 | `GDX_Close` | VanEck Gold Miners ETF - daily close |
| 10 | `USO_Close` | United States Oil Fund ETF - daily close |
| 11 | `RHO_PRICE` | Rhodium spot price |

</details>

---

## 🗂️ Project Structure

```
Gold_Price_Prediction/
│
├── 📄 app.py                  ← Flask app, model training & API routes
├── 📋 requirements.txt        ← Python dependencies
├── 📓 Gold_predict.ipynb      ← EDA, model comparison, elbow-curve analysis
│
├── 📂 Dataset/
│   └── FINAL_USO.csv          ← Historical market data (2011–2018)
│
├── 📂 templates/
│   ├── index.html             ← Home - stats dashboard
│   ├── predict.html           ← Prediction form with live results
│   └── about.html             ← Methodology & feature breakdown
│
└── 📂 static/
    └── style.css              ← Global stylesheet (gold-accented theme)
```

---

## ⚙️ Getting Started

### Prerequisites

- Python **3.8+**
- pip

### 1 - Clone the Repository

```bash
git clone https://github.com/anubhab1601/Gold_Price_Prediction.git
cd Gold_Price_Prediction
```

### 2 - Create & Activate a Virtual Environment

```bash
# Create
python -m venv venv

# Activate - Windows
venv\Scripts\activate

# Activate - macOS / Linux
source venv/bin/activate
```

### 3 - Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 - Run the App

```bash
python app.py
```

Open **http://127.0.0.1:5001** in your browser. 🎉

---

## 🔌 API Reference

### `POST /api/predict`

Accepts market indicator values and returns the predicted GLD closing price.

**Request**

```http
POST /api/predict
Content-Type: application/json
```

```json
{
  "sp_close":   185.0,
  "dj_close":   17500.0,
  "eu_price":   1.15,
  "of_price":   55.0,
  "sf_price":   50000.0,
  "plt_price":  1100.0,
  "pld_price":  750.0,
  "usdi_price": 92.0,
  "gdx_close":  25.0,
  "uso_close":  18.0,
  "rho_price":  1200.0
}
```

**Response - 200 OK**

```json
{
  "success": true,
  "predicted_close": 124.76,
  "inputs": {
    "SP_close": 185.0,
    "DJ_close": 17500.0,
    "EU_Price": 1.15,
    "OF_Price": 55.0,
    "SF_Price": 50000.0,
    "PLT_Price": 1100.0,
    "PLD_Price": 750.0,
    "USDI_Price": 92.0,
    "GDX_Close": 25.0,
    "USO_Close": 18.0,
    "RHO_PRICE": 1200.0
  }
}
```

**Response - 400 Bad Request**

```json
{
  "success": false,
  "error": "could not convert string to float: 'abc'"
}
```

---

### `GET /api/stats`

Returns dataset statistics and live model performance metrics.

```http
GET /api/stats
```

```json
{
  "total_records": 1718,
  "date_start": "Jan 02, 2011",
  "date_end":   "Dec 31, 2018",
  "r2":   0.9983,
  "mae":  0.59,
  "rmse": 1.1,
  "best_model": "KNN (n_neighbors=2)"
}
```

---

## 📓 Notebook

`Gold_predict.ipynb` walks through the full ML pipeline:

| Section | Content |
|:---|:---|
| **EDA** | Distributions, box plots, correlation heatmap, outlier analysis |
| **Feature Engineering** | Selection of the 11 most predictive indicators |
| **Model Comparison** | Linear Regression vs SVR vs Random Forest vs KNN |
| **Elbow Curve** | RMSE vs `k` (1–20) to identify optimal `k = 2` |
| **Final Evaluation** | MAE, MSE, RMSE, R² on held-out test set |

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "feat: add amazing feature"
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request** 🚀

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

**Built with 💛 by [Anubhab](https://github.com/anubhab1601)**

<br/>

If this project helped you, please consider giving it a ⭐ - it means a lot!

<br/>

[![GitHub followers](https://img.shields.io/github/followers/anubhab1601?style=social)](https://github.com/anubhab1601)

</div>

