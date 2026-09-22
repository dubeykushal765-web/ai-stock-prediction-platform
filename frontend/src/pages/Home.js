import React, { useEffect, useState } from "react";
import { getTopStocks } from "../services/api";

function Home() {
  const [stocks, setStocks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getTopStocks()
      .then((response) => {
        setStocks(response.data.stocks);
        setLoading(false);
      })
      .catch((err) => {
        setError("Failed to load stocks. Please try again later.");
        setLoading(false);
      });
  }, []);

  if (loading) return <div style={{ padding: "2rem" }}>Loading top stocks...</div>;
  if (error) return <div style={{ padding: "2rem", color: "red" }}>{error}</div>;

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Top Stocks</h1>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>Symbol</th>
            <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>Current Price</th>
            <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>Predicted Price</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock) => (
            <tr key={stock.symbol}>
              <td style={{ padding: "0.5rem 0" }}>{stock.symbol}</td>
              <td>${stock.current_price}</td>
              <td>${stock.predicted_price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Home;