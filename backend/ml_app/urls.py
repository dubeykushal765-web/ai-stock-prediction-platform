from django.urls import path
from .views import predict_stock, stock_history, top_stocks

urlpatterns = [
    path('predict-stock/', predict_stock),
    path('stock-history/', stock_history),
    path('top-stocks/', top_stocks),
]