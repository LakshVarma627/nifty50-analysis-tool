import { useEffect } from 'react';
import { useWebSocket as useWS } from 'react-websocket';

export const useWebSocket = (url) => {
  const { lastMessage, readyState } = useWS(url, {
    shouldReconnect: () => true,
    reconnectInterval: 3000
  });

  return {
    lastMessage,
    isConnected: readyState === 1
  };
};