import { Server } from 'mock-socket';

const generateMockCandle = () => ({
  x: new Date().toISOString(),
  y: [
    Math.random() * 18000 + 17000,
    Math.random() * 18100 + 17000,
    Math.random() * 17900 + 17000,
    Math.random() * 18050 + 17000
  ]
});

const generateMockRecommendation = () => ({
  prediction: Math.random(),
  wolfram_analysis: "Volatility analysis suggests 68% probability of upward movement based on Black-Scholes model"
});

export const startMockWebSocket = () => {
  const mockServer = new Server(import.meta.env.VITE_WS_URL);
  const recommendationServer = new Server(import.meta.env.VITE_RECOMMENDATION_WS_URL);

  mockServer.on('connection', (socket) => {
    setInterval(() => {
      socket.send(JSON.stringify(generateMockCandle()));
    }, 1000);
  });

  recommendationServer.on('connection', (socket) => {
    setInterval(() => {
      socket.send(JSON.stringify(generateMockRecommendation()));
    }, 5000);
  });
};