import React from 'react';
import { BarChart } from 'recharts';

const SentimentGraph = ({ sentimentData }) => {
  return (
    <div>
      <h3>News Sentiment Analysis</h3>
      <BarChart data={sentimentData} />
    </div>
  );
};

export default SentimentGraph;
