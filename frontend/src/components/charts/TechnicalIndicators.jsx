import { useEffect, useState } from 'react';
import { useWebSocket } from '../../hooks/useWebSocket';
import ApexCharts from 'react-apexcharts';

export default function TechnicalIndicators() {
  const [indicators, setIndicators] = useState({
    rsi: [],
    macd: { macd: [], signal: [] }
  });
  const { lastMessage } = useWebSocket(import.meta.env.VITE_WS_URL);

  useEffect(() => {
    if (lastMessage) {
      const data = JSON.parse(lastMessage.data);
      setIndicators({
        rsi: [...indicators.rsi.slice(-50), data.rsi],
        macd: {
          macd: [...indicators.macd.macd.slice(-50), data.macd],
          signal: [...indicators.macd.signal.slice(-50), data.signal]
        }
      });
    }
  }, [lastMessage]);

  return (
    <ApexCharts
      options={{
        chart: { type: 'line' },
        xaxis: { type: 'datetime' }
      }}
      series={[
        { name: 'RSI', data: indicators.rsi },
        { name: 'MACD', data: indicators.macd.macd },
        { name: 'Signal', data: indicators.macd.signal }
      ]}
      type="line"
      height={300}
    />
  );
}