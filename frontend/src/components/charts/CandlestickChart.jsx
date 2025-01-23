import { useEffect, useState } from 'react';
import { useWebSocket } from '../../hooks/useWebSocket';
import ApexCharts from 'react-apexcharts';

export default function CandlestickChart() {
  const [series, setSeries] = useState([{ data: [] }]);
  const { lastMessage } = useWebSocket(import.meta.env.VITE_WS_URL);

  useEffect(() => {
    if (lastMessage) {
      const newData = JSON.parse(lastMessage.data);
      setSeries([{
        data: [...series[0].data.slice(-100), newData]
      }]);
    }
  }, [lastMessage]);

  return (
    <ApexCharts
      options={{
        chart: { type: 'candlestick' },
        xaxis: { type: 'datetime' }
      }}
      series={series}
      type="candlestick"
      height={500}
    />
  );
}