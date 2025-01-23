import React from 'react';
import { LineChart } from 'recharts';

const PredictionChart = ({ predictions }) => {
  return (
    <div>
      <h3>Stock Price Predictions</h3>
      <LineChart data={predictions} />
    </div>
  );
};

export default PredictionChart;
