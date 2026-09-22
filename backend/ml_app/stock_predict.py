import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
from curl_cffi import requests as cffi_requests

session = cffi_requests.Session(impersonate="chrome")


def predict_stock_price(symbol):

    stock = yf.Ticker(symbol, session=session)
    data = stock.history(period="3mo")

    if data.empty:
        return None

    data = data.reset_index()

    data["day"] = np.arange(len(data))

    X = data[["day"]]
    y = data["Close"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(data)]])

    predicted_price = model.predict(next_day)[0]

    return round(predicted_price, 2)