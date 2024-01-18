import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Akciju prognozēšanas klases definēšana.
class StockPredictor:
    # Inicializēt klasi ar tikera simbolu un lineārās regresijas modeli.
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.model = LinearRegression()

    # Vēsturisko datu iegūšana no Yahoo Finance par doto tikera simbolu.
    def fetch_data(self, start_date):
        ticker_data = yf.Ticker(self.ticker_symbol)
        data = ticker_data.history(period='1d', start=start_date, end=datetime.now())
        return data[['Close']].rename(columns={'Close': 'Price'})

    # Datu pirmapstrāde, atiestatot indeksu un pārveidojot datumu par kārtas numuru.
    def preprocess(self, data):
        data.reset_index(inplace=True)
        data['DateOrd'] = data['Date'].apply(lambda x: x.toordinal())
        return data

    # Lineārās regresijas modeļa apmācība.
    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        self.model.fit(X_train, y_train)

    # Akciju cenu prognozēšana nākamajām 10 dienām.
    def predict_next_days(self, days=10):
        last_date = datetime.now().date()
        next_days = np.array([(last_date + timedelta(days=i)).toordinal() for i in range(1, days+1) if (last_date + timedelta(days=i)) > last_date]).reshape(-1, 1)
        return self.model.predict(next_days)



    # Faktisko un prognozēto akciju cenu grafika izveide.
    def plot_predictions(self, data, predictions):
        plt.plot(data['Date'], data['Price'], label='Actual Price')
        future_dates = pd.date_range(start=data['Date'].iloc[-1], periods=len(predictions)+1)[1:]
        plt.plot(future_dates, predictions, color='red', label='Predicted Price')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Actual and Predicted Prices')
        plt.legend()
        plt.show()

    # Faktisko un prognozēto akciju cenu saglabāšana Excel failā.
    def save_to_excel(self, data, predictions, filename):
        # Konvertēt kolonnu "Datums" uz virkni un noņem laiku.
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
        # Pievienot jaunu kolonnu krājuma nosaukumam.
        data['Name'] = self.ticker_symbol
        # Izveidot jaunu DataFrame prognozētajām cenām.
        future_dates = pd.date_range(start=data['Date'].iloc[-1], periods=len(predictions)+1)[1:]
        predicted_data = pd.DataFrame({
            'Date': future_dates.strftime('%Y-%m-%d'),
            'Name': self.ticker_symbol,
            'Price': np.nan,
            'Predicted Price': predictions.flatten()
        })
        # Konkatenēt neapstrādātos datus ar prognozētajiem datiem.
        full_data = pd.concat([data, predicted_data])
        # Saglabāt "Datums", "Nosaukums", "Cena" un "Prognozētā cena" kolonnas Excel failā.
        full_data[['Date', 'Name', 'Price', 'Predicted Price']].to_excel(filename, index=False)


# Pamatfunkcija krājumu prognozēšanas veikšanai.
if __name__ == "__main__":
    predictor = StockPredictor('NKE') # Inicializēt StockPredictor klasi ar "NKE" kā tikera simbolu.
    data = predictor.fetch_data(datetime.now() - timedelta(days=30)) # Vēsturisko datu iegūšana no 2023. gada 1. decembra.
    data = predictor.preprocess(data) # Datu pirmapstrāde.
    predictor.train(data['DateOrd'].values.reshape(-1,1), data['Price'].values.reshape(-1,1)) # Modeļa apmācība.
    predictions = predictor.predict_next_days(10) # Akciju cenu prognozēšana nākamajām 10 dienām.
    predictor.plot_predictions(data, predictions) # Konstruēt faktisko un prognozēto akciju cenu grafiku.
    predictor.save_to_excel(data, predictions, 'stock_data.xlsx') # Faktisko un prognozēto akciju cenu saglabāšana Excel failā.
