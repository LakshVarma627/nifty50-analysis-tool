import React, { useState, useEffect } from 'react';
import { useWebSocket } from 'react-websocket';

export default function CandlestickChart() {
  const [data, setData] = useState([]);
  const { lastMessage } = useWebSocket('wss://your-api/ws');

  useEffect(() => {
    if (lastMessage) {
      const newData = JSON.parse(lastMessage.data);
      setData((prev) => [...prev.slice(-100), newData]); // Keep last 100 data points
    }
  }, [lastMessage]);

  return (
    <div className="chart-container">
      <h3>Real-Time Nifty50 Candlestick Chart</h3>
      <div className="chart">
        {data.map((item, idx) => (
          <div key={idx} className="candle">
            <div className="candle-body" style={{ height: `${item.close - item.open}px` }} />
            <div className="candle-wick" style={{ height: `${item.high - item.low}px` }} />
          </div>
        ))}
      </div>
    </div>
  );
}