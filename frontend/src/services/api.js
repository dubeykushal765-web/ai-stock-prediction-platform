import axios from "axios";

const API_BASE_URL = "https://ai-stock-prediction-platform.onrender.com/api";

export const getTopStocks = () => {
  return axios.get(`${API_BASE_URL}/top-stocks/`);
};

export const getStockPrediction = (symbol) => {
  return axios.get(`${API_BASE_URL}/predict-stock/`, {
    params: { symbol },
  });
};

export const getStockHistory = (symbol) => {
  return axios.get(`${API_BASE_URL}/stock-history/`, {
    params: { symbol },
  });
};