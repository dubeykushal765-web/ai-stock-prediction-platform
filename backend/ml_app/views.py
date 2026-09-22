from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .yahoo_client import get_chart_data
from .stock_predict import predict_stock_price


@api_view(['GET'])
def predict_stock(request):

    symbol = request.GET.get("symbol", "AAPL")

    points = get_chart_data(symbol, range_="1d", interval="1d")

    if not points:
        return Response({"error": "Invalid stock symbol"})

    current_price = points[-1][1]

    predicted_price = predict_stock_price(symbol)

    return Response({
        "symbol": symbol,
        "current_price": current_price,
        "predicted_price": predicted_price
    })


@api_view(['GET'])
def stock_history(request):

    symbol = request.GET.get("symbol", "AAPL")

    points = get_chart_data(symbol, range_="1mo", interval="1d")

    if not points:
        return Response({"error": "Invalid stock symbol"})

    history = []
    for ts, price in points:
        date_str = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
        history.append({
            "date": date_str,
            "price": price
        })

    return Response({
        "symbol": symbol,
        "history": history
    })


@api_view(['GET'])
def top_stocks(request):

    stocks = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN"]

    results = []

    for symbol in stocks:

        points = get_chart_data(symbol, range_="1d", interval="1d")

        if not points:
            continue

        current_price = points[-1][1]

        predicted_price = predict_stock_price(symbol)

        results.append({
            "symbol": symbol,
            "current_price": current_price,
            "predicted_price": predicted_price
        })

    return Response({
        "stocks": results
    })