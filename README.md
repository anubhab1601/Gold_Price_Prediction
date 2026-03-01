<div align="center">

# 🥇 Gold Price Prediction

### AI-powered GLD ETF price forecasting using K-Nearest Neighbours Regression

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

> Predict the **GLD (Gold ETF) closing price** in real time using 11 global market indicators,  
> trained on 7 years of daily trading data (2011 – 2018).

</div>

---

## 📸 Preview

| Home | Predict | About |
|:---:|:---:|:---:|
| Dataset stats & model metrics at a glance | Interactive form with real-time prediction | Full methodology & feature breakdown |

---

## 🚀 Live Demo

Run locally → `http://127.0.0.1:5001`

---

## ✨ Features

- **Real-time prediction** — enter market indicators and get an instant GLD price estimate  
- **KNN Regression model** with optimal `k = 2` selected via elbow-curve analysis  
- **High accuracy** — R² ≈ 0.99+ on test set  
- **Responsive UI** — clean, modern design with Inter font & Font Awesome icons  
- **REST API** — `/api/predict` JSON endpoint for programmatic access  
- **Live model metrics** — MAE, MSE, RMSE, and R² surfaced directly in the UI  

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | K-Nearest Neighbours Regressor |
| Optimal `k` | 2 (elbow curve, k = 1–20) |
| Feature Scaling | StandardScaler (fit on train set only) |
| Train / Test Split | 80 % / 20 %, `random_state = 0` |
| R² Score | ≈ 0.9983 |
| MAE | ≈ $0.59 |
| RMSE | ≈ $1.10 |

---

## 📊 Dataset

| Property | Detail |
|---|---|
| File | `Dataset/FINAL_USO.csv` |
| Records | 1,718 daily rows |
| Date Range | Jan 2011 – Dec 2018 |
| Total Columns | 81 |
| Features Used | 11 (see below) |
| Target | `Close` — GLD ETF daily closing price (USD) |
| Missing Values | None |
| Duplicates | None |

### 🔑 11 Input Features

| Feature | Description |
|---|---|
| `SP_close` | S&P 500 Index daily close |
| `DJ_close` | Dow Jones Industrial Average daily close |
| `EU_Price` | EUR / USD exchange rate |
| `OF_Price` | Oil Futures price (USD/barrel) |
| `SF_Price` | Silver Futures price |
| `PLT_Price` | Platinum Futures price |
| `PLD_Price` | Palladium Futures price |
| `USDI_Price` | US Dollar Index |
| `GDX_Close` | VanEck Gold Miners ETF close |
| `USO_Close` | United States Oil Fund ETF close |
| `RHO_PRICE` | Rhodium spot price |

---

## 🗂️ Project Structure

```
Gold_Price_Prediction/
│
├── app.py                  # Flask application & KNN model training
├── requirements.txt        # Python dependencies
│
├── Dataset/
│   └── FINAL_USO.csv       # Historical market data (2011–2018)
│
├── templates/
│   ├── index.html          # Home page — stats dashboard
│   ├── predict.html        # Prediction form
│   └── about.html          # Methodology & feature info
│
├── static/
│   └── style.css           # Global stylesheet
│
└── Gold_predict.ipynb      # EDA, model comparison & elbow-curve notebook
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher  
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/anubhab1601/Gold_Price_Prediction.git
cd Gold_Price_Prediction

# 2. (Recommended) Create & activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open your browser at **http://127.0.0.1:5001** 🎉

---

## 🔌 API Reference

### `POST /api/predict`

Returns the predicted GLD closing price for the supplied market indicators.

**Request body (JSON):**

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

**Response (JSON):**

```json
{
  "success": true,
  "predicted_close": 124.76,
  "inputs": { ... }
}
```

### `GET /api/stats`

Returns dataset statistics and model performance metrics as JSON.

---

## 📓 Notebook

`Gold_predict.ipynb` contains:

- Exploratory Data Analysis (EDA) — distributions, correlations, outlier checks  
- Comparison of multiple regression algorithms  
- Elbow-curve analysis (`k = 1–20`) to identify the optimal KNN `k`  
- Final model training and evaluation  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/your-feature`  
3. Commit your changes: `git commit -m 'Add some feature'`  
4. Push to the branch: `git push origin feature/your-feature`  
5. Open a Pull Request  

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ by **[Anubhab](https://github.com/anubhab1601)**

⭐ Star the repo if you found it useful!

</div>
