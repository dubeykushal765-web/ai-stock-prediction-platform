import numpy as np
from sklearn.linear_model import LinearRegression
from .yahoo_client import get_chart_data


def predict_stock_price(symbol):

    points = get_chart_data(symbol, range_="3mo", interval="1d")

    if not points:
        return None

    prices = [p[1] for p in points]

    X = np.arange(len(prices)).reshape(-1, 1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(prices)]])

    predicted_price = model.predict(next_day)[0]

    return round(predicted_price, 2)