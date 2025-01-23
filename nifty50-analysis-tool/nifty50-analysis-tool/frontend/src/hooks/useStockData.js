import { useEffect, useState } from 'react';  
import { getNiftyData } from '../services/stockApi';  

export const useStockData = () => {  
  const [data, setData] = useState(null);  
  const [error, setError] = useState('');  

  useEffect(() => {  
    const fetchData = async () => {  
      try {
        const response = await getNiftyData();  
        if (response.error) setError(response.error);  
        else setData(response);  
      } catch (err) {
        setError('Failed to fetch data. Please try again.');
      }
    };  
    fetchData();  

    // Auto-refresh every 60s  
    const interval = setInterval(fetchData, 60000);  
    return () => clearInterval(interval);  
  }, []);  

  return { data, error };  
};  
