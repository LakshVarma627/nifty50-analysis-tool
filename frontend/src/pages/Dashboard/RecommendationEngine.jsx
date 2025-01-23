import React, { useState, useEffect } from 'react';
import { useWebSocket } from 'react-websocket';

export default function RecommendationEngine() {
  const [recommendation, setRecommendation] = useState(null);
  const { lastMessage } = useWebSocket('wss://your-api/recommendations');

  useEffect(() => {
    if (lastMessage) {
      const data = JSON.parse(lastMessage.data);
      setRecommendation({
        signal: data.prediction > 0.7 ? 'BUY' : data.prediction < 0.3 ? 'SELL' : 'HOLD',
        confidence: Math.round(data.prediction * 100),
      });
    }
  }, [lastMessage]);

  return (
    <div className="recommendation-panel">
      <h3>AI Trading Recommendations</h3>
      {recommendation ? (
        <>
          <div className={`signal ${recommendation.signal.toLowerCase()}`}>
            {recommendation.signal}
          </div>
          <div className="confidence">Confidence: {recommendation.confidence}%</div>
        </>
      ) : (
        <div className="loading">Analyzing market data...</div>
      )}
    </div>
  );
}