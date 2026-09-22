import React, { useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import { getStockPrediction, getStockHistory } from "../services/api";

function Dashboard() {
  const [symbol, setSymbol] = useState("");
  const [prediction, setPrediction] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = (e) => {
    e.preventDefault();
    if (!symbol.trim()) return;

    setLoading(true);
    setError(null);
    setPrediction(null);
    setHistory([]);

    Promise.all([getStockPrediction(symbol), getStockHistory(symbol)])
      .then(([predictionRes, historyRes]) => {
        if (predictionRes.data.error || historyRes.data.error) {
          setError("Invalid stock symbol. Please try again.");
        } else {
          setPrediction(predictionRes.data);
          setHistory(historyRes.data.history);
        }
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to fetch data. Please try again later.");
        setLoading(false);
      });
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Stock Dashboard</h1>
      <form onSubmit={handleSearch} style={{ marginBottom: "2rem" }}>
        <input
          type="text"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value.toUpperCase())}
          placeholder="Enter stock symbol (e.g. AAPL)"
          style={{ padding: "0.5rem", marginRight: "1rem", width: "250px" }}
        />
        <button type="submit" style={{ padding: "0.5rem 1rem" }}>
          Search
        </button>
      </form>

      {loading && <div>Loading...</div>}
      {error && <div style={{ color: "red" }}>{error}</div>}

      {prediction && (
        <div style={{ marginBottom: "2rem" }}>
          <h2>{prediction.symbol}</h2>
          <p>Current Price: ${prediction.current_price}</p>
          <p>Predicted Price: ${prediction.predicted_price}</p>
        </div>
      )}

      {history.length > 0 && (
        <div style={{ width: "100%", height: 400 }}>
          <ResponsiveContainer>
            <LineChart data={history}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis domain={["auto", "auto"]} />
              <Tooltip />
              <Line type="monotone" dataKey="price" stroke="#1a1a2e" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}

export default Dashboard;