import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_chart_data(symbol, range_="1mo", interval="1d"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    params = {"range": range_, "interval": interval}

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return None

    result = data.get("chart", {}).get("result")
    if not result:
        return None

    result = result[0]
    timestamps = result.get("timestamp")
    closes = result.get("indicators", {}).get("quote", [{}])[0].get("close")

    if not timestamps or not closes:
        return None

    points = []
    for ts, close in zip(timestamps, closes):
        if close is not None:
            points.append((ts, round(close, 2)))

    return points if points else None