import { useEffect, useState } from 'react';
import { useWebSocket } from '../../hooks/useWebSocket';

export default function RecommendationEngine() {
  const [recommendation, setRecommendation] = useState(null);
  const { lastMessage } = useWebSocket(import.meta.env.VITE_RECOMMENDATION_WS_URL);

  useEffect(() => {
    if (lastMessage) {
      const data = JSON.parse(lastMessage.data);
      setRecommendation({
        signal: data.prediction > 0.7 ? 'BUY' : data.prediction < 0.3 ? 'SELL' : 'HOLD',
        confidence: Math.round(data.prediction * 100),
        reasoning: data.wolfram_analysis
      });
    }
  }, [lastMessage]);

  return (
    <div className="recommendation-card">
      <h3>AI Trading Signal</h3>
      {recommendation ? (
        <>
          <div className={`signal ${recommendation.signal.toLowerCase()}`}>
            {recommendation.signal} ({recommendation.confidence}%)
          </div>
          <div className="analysis">
            <h4>Wolfram Analysis</h4>
            <p>{recommendation.reasoning}</p>
          </div>
        </>
      ) : (
        <div className="loading">Analyzing market patterns...</div>
      )}
    </div>
  );
}