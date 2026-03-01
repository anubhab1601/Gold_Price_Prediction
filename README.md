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

- [🔍 Overview](#-overview)
- [🌐 Live Demo](#-live-demo)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🧠 How It Works](#-how-it-works)
- [📊 Model Performance](#-model-performance)
- [📁 Dataset Overview](#-dataset-overview)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Getting Started](#️-getting-started)
- [🚀 Usage](#-usage)
- [ Notebook](#-notebook)
- [📈 EDA Highlights](#-eda-highlights)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🔍 Overview

This project builds a complete **end-to-end machine learning pipeline** to predict the price of the **GLD ETF (Gold Exchange-Traded Fund)** based on correlated global market indicators.

The workflow covers:

1. **Exploratory Data Analysis (EDA)** - distributions, trends, outlier detection, and correlation analysis
2. **Model Training & Comparison** - Linear Regression, Decision Tree, Random Forest, and KNN evaluated head-to-head
3. **Model Selection** - KNN (k=2) selected via elbow-curve analysis for the lowest error
4. **Web Application** - Interactive Flask app where users enter market values and get an instant GLD price prediction

---

## 🌐 Live Demo

> Run locally following the [Getting Started](#️-getting-started) steps below.

| Route | Page | Description |
|:---:|:---|:---|
| `/` | **Home** | Project overview, dataset statistics & live model metrics |
| `/predict` | **Predict** | Enter 11 market values → get instant GLD price estimate |
| `/about` | **About** | Dataset info, model details & feature breakdown |

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

All models trained on **80%** of the data and evaluated on the remaining **20%** (`random_state=0`).

<div align="center">

| Model | R² | MAE | RMSE |
|:---|:---:|:---:|:---:|
| 🥇 **KNN (k=2)** ← _selected_ | **0.9983** | **$0.59** | **$1.10** |
| Random Forest | 0.9961 | $0.78 | $1.41 |
| Decision Tree | 0.9934 | $0.91 | $1.83 |
| Multiple Linear Regression | 0.9612 | $2.44 | $4.45 |
| Simple Linear Regression | 0.8741 | $4.37 | $8.01 |

</div>

> **KNN with k=2** was selected as the best model based on elbow-curve analysis (k=1 to 20).  
> It explains **99.83%** of variance in GLD closing prices on completely unseen test data.

---

## 📁 Dataset Overview

| Property | Detail |
|:---|:---|
| **Source** | [Kaggle - Gold Price Prediction Dataset](https://www.kaggle.com/datasets/sid321axn/gold-price-prediction-dataset) |
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

| # | Feature | Description | Correlation w/ GLD |
|:---:|:---|:---|:---:|
| 1 | `SP_close` | S&P 500 Index - daily closing value | +0.63 |
| 2 | `DJ_close` | Dow Jones Industrial Average - daily close | +0.61 |
| 3 | `EU_Price` | EUR / USD exchange rate | -0.51 |
| 4 | `OF_Price` | Crude Oil Futures price (USD / barrel) | +0.29 |
| 5 | `SF_Price` | Silver Futures price | **+0.87** |
| 6 | `PLT_Price` | Platinum Futures price | +0.55 |
| 7 | `PLD_Price` | Palladium Futures price | +0.38 |
| 8 | `USDI_Price` | US Dollar Index | -0.74 |
| 9 | `GDX_Close` | VanEck Gold Miners ETF - daily close | **+0.92** |
| 10 | `USO_Close` | United States Oil Fund ETF - daily close | -0.19 |
| 11 | `RHO_PRICE` | Rhodium spot price | +0.41 |

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

## � Usage

### Predict via the Web UI

Navigate to **http://127.0.0.1:5001/predict**, fill in the 11 market indicator fields, and click **Predict**.

### Run the Jupyter Notebook (EDA)

```bash
jupyter notebook Gold_predict.ipynb
```



## 📓 Notebook

`Gold_predict.ipynb` walks through the full ML pipeline:

| Section | Content |
|:---|:---|
| **EDA** | Distributions, box plots, correlation heatmap, pairplot, outlier analysis |
| **Feature Engineering** | Selection of the 11 most predictive market indicators |
| **Model Comparison** | Simple LR, Multiple LR, Decision Tree, Random Forest, KNN |
| **Elbow Curve** | RMSE vs `k` (1–20) to identify optimal `k = 2` |
| **Final Evaluation** | MAE, MSE, RMSE, R² on held-out test set |

---

## 📈 EDA Highlights

- **No missing values** and **no duplicate rows** found in the dataset
- **GDX_Close** (Gold Miners ETF) has the strongest positive correlation with GLD (`+0.92`)
- **SF_Price** (Silver) is the second most correlated feature (`+0.87`)
- **USDI_Price** (US Dollar Index) shows the strongest inverse relationship (`-0.74`)
- **USO_Close** (Oil ETF) has the highest negative correlation among commodity features (`-0.19`)
- Outlier analysis performed via IQR method on skewed distributions
- Heatmap confirms multicollinearity between equity indices (SP_close, DJ_close)

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

**Built with ❤️ by [Anubhab](https://github.com/anubhab1601)**

<br/>

If this project helped you, please consider giving it a ⭐ - it means a lot!

<br/>

[![GitHub followers](https://img.shields.io/github/followers/anubhab1601?style=social)](https://github.com/anubhab1601)

</div>


