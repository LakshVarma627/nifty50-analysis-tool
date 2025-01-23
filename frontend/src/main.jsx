import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { startMockWebSocket } from './services/mockData';

// Start mock WebSocket server in development
if (import.meta.env.MODE === 'development') {
  startMockWebSocket();
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);