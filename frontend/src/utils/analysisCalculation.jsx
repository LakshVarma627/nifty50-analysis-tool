export const calculateRSI = (prices) => {
  const gains = [];
  const losses = [];
  for (let i = 1; i < prices.length; i++) {
    const change = prices[i] - prices[i - 1];
    if (change > 0) gains.push(change);
    else losses.push(Math.abs(change));
  }
  const avgGain = gains.reduce((a, b) => a + b, 0) / gains.length;
  const avgLoss = losses.reduce((a, b) => a + b, 0) / losses.length;
  return 100 - (100 / (1 + (avgGain / avgLoss)));
};