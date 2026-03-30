from rest_framework.decorators import api_view
from rest_framework.response import Response
import yfinance as yf
from .stock_predict import predict_stock_price


@api_view(['GET'])
def predict_stock(request):

    symbol = request.GET.get("symbol", "AAPL")

    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")

    if data.empty:
        return Response({"error": "Invalid stock symbol"})

    current_price = round(data["Close"].iloc[-1], 2)

    predicted_price = predict_stock_price(symbol)

    return Response({
        "symbol": symbol,
        "current_price": current_price,
        "predicted_price": predicted_price
    })


@api_view(['GET'])
def stock_history(request):

    symbol = request.GET.get("symbol", "AAPL")

    stock = yf.Ticker(symbol)
    data = stock.history(period="1mo")

    if data.empty:
        return Response({"error": "Invalid stock symbol"})

    history = []

    for index, row in data.iterrows():
        history.append({
            "date": str(index.date()),
            "price": round(row["Close"], 2)
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

        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data.empty:
            continue

        current_price = round(data["Close"].iloc[-1], 2)

        predicted_price = predict_stock_price(symbol)

        results.append({
            "symbol": symbol,
            "current_price": current_price,
            "predicted_price": predicted_price
        })

    return Response({
        "stocks": results
    })