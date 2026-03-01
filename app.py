from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

app = Flask(__name__)

FEATURES = [
    'SP_close', 'DJ_close', 'EU_Price', 'OF_Price', 'SF_Price',
    'PLT_Price', 'PLD_Price', 'USDI_Price', 'GDX_Close', 'USO_Close', 'RHO_PRICE'
]

# ── Load dataset and train model ──────────────────────────────────────────────
def load_and_train():
    df = pd.read_csv("Dataset/FINAL_USO.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)

    x = df[FEATURES].values
    y = df['Close'].values

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0
    )

    sc = StandardScaler()
    x_train_sc = sc.fit_transform(x_train)
    x_test_sc  = sc.transform(x_test)

    # KNN with optimal k = 2 (from elbow curve in notebook)
    knn = KNeighborsRegressor(n_neighbors=2)
    knn.fit(x_train_sc, y_train)

    y_pred = knn.predict(x_test_sc)

    metrics = {
        'r2'  : round(float(r2_score(y_test, y_pred)), 4),
        'mae' : round(float(mean_absolute_error(y_test, y_pred)), 4),
        'mse' : round(float(mean_squared_error(y_test, y_pred)), 4),
        'rmse': round(float(np.sqrt(mean_squared_error(y_test, y_pred))), 4),
    }

    stats = {
        'total_records': int(df.shape[0]),
        'date_start'   : df['Date'].min().strftime('%b %d, %Y'),
        'date_end'     : df['Date'].max().strftime('%b %d, %Y'),
        # Target (GLD Close) stats
        'close_min' : round(float(df['Close'].min()), 2),
        'close_max' : round(float(df['Close'].max()), 2),
        'close_mean': round(float(df['Close'].mean()), 2),
        'close_std' : round(float(df['Close'].std()), 2),
        # Feature ranges
        'sp_min'  : round(float(df['SP_close'].min()), 2),
        'sp_max'  : round(float(df['SP_close'].max()), 2),
        'dj_min'  : round(float(df['DJ_close'].min()), 2),
        'dj_max'  : round(float(df['DJ_close'].max()), 2),
        'eu_min'  : round(float(df['EU_Price'].min()), 4),
        'eu_max'  : round(float(df['EU_Price'].max()), 4),
        'of_min'  : round(float(df['OF_Price'].min()), 2),
        'of_max'  : round(float(df['OF_Price'].max()), 2),
        'sf_min'  : round(float(df['SF_Price'].min()), 2),
        'sf_max'  : round(float(df['SF_Price'].max()), 2),
        'plt_min' : round(float(df['PLT_Price'].min()), 2),
        'plt_max' : round(float(df['PLT_Price'].max()), 2),
        'pld_min' : round(float(df['PLD_Price'].min()), 2),
        'pld_max' : round(float(df['PLD_Price'].max()), 2),
        'usdi_min': round(float(df['USDI_Price'].min()), 2),
        'usdi_max': round(float(df['USDI_Price'].max()), 2),
        'gdx_min' : round(float(df['GDX_Close'].min()), 2),
        'gdx_max' : round(float(df['GDX_Close'].max()), 2),
        'uso_min' : round(float(df['USO_Close'].min()), 2),
        'uso_max' : round(float(df['USO_Close'].max()), 2),
        'rho_min' : round(float(df['RHO_PRICE'].min()), 2),
        'rho_max' : round(float(df['RHO_PRICE'].max()), 2),
        # Dataset means for the 6 hidden features (used as defaults when UI sends only top-5)
        'sp_mean'  : round(float(df['SP_close'].mean()), 2),
        'dj_mean'  : round(float(df['DJ_close'].mean()), 2),
        'eu_mean'  : round(float(df['EU_Price'].mean()), 4),
        'pld_mean' : round(float(df['PLD_Price'].mean()), 2),
        'uso_mean' : round(float(df['USO_Close'].mean()), 2),
        'rho_mean' : round(float(df['RHO_PRICE'].mean()), 2),
        # Model info
        'best_model': 'KNN (n_neighbors=2)',
        'optimal_k' : 2,
        **metrics,
    }

    return knn, sc, stats

# Initialise once at startup
knn_model, scaler, dataset_stats = load_and_train()

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html', stats=dataset_stats)

@app.route('/predict')
def predict_page():
    return render_template('predict.html', stats=dataset_stats)

@app.route('/about')
def about():
    return render_template('about.html', stats=dataset_stats)

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        d = request.json

        sp_close   = float(d.get('sp_close',   185.0))
        dj_close   = float(d.get('dj_close',   17500.0))
        eu_price   = float(d.get('eu_price',   1.15))
        of_price   = float(d.get('of_price',   55.0))
        sf_price   = float(d.get('sf_price',   50000.0))
        plt_price  = float(d.get('plt_price',  1100.0))
        pld_price  = float(d.get('pld_price',  750.0))
        usdi_price = float(d.get('usdi_price', 92.0))
        gdx_close  = float(d.get('gdx_close',  25.0))
        uso_close  = float(d.get('uso_close',  18.0))
        rho_price  = float(d.get('rho_price',  1200.0))

        user_input = np.array([[
            sp_close, dj_close, eu_price, of_price, sf_price,
            plt_price, pld_price, usdi_price, gdx_close, uso_close, rho_price
        ]])
        user_scaled = scaler.transform(user_input)

        predicted = float(knn_model.predict(user_scaled)[0])

        return jsonify({
            'success'         : True,
            'predicted_close' : round(predicted, 2),
            'inputs': {
                'SP_close'   : sp_close,
                'DJ_close'   : dj_close,
                'EU_Price'   : eu_price,
                'OF_Price'   : of_price,
                'SF_Price'   : sf_price,
                'PLT_Price'  : plt_price,
                'PLD_Price'  : pld_price,
                'USDI_Price' : usdi_price,
                'GDX_Close'  : gdx_close,
                'USO_Close'  : uso_close,
                'RHO_PRICE'  : rho_price,
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/stats')
def get_stats():
    return jsonify(dataset_stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
