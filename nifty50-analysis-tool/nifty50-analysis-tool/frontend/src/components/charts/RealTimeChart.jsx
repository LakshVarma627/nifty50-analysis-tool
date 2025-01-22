import { createChart } from 'lightweight-charts';  
import { useEffect, useRef } from 'react';  

export default function RealTimeChart({ data }) {  
  const chartContainerRef = useRef(null);  

  useEffect(() => {  
    if (!chartContainerRef.current || !data) return;  

    const chart = createChart(chartContainerRef.current, {  
      width: 800,  
      height: 400,  
      timeScale: { timeVisible: true },  
    });  

    const candleSeries = chart.addCandlestickSeries();  
    candleSeries.setData(data);  

    return () => chart.remove(); // Cleanup  
  }, [data]);  

  return <div ref={chartContainerRef} />;  
}  