import { useEffect, useState } from 'react';  
import { getNiftyData } from '../services/stockApi';  

export const useStockData = () => {  
  const [data, setData] = useState(null);  
  const [error, setError] = useState('');  

  useEffect(() => {  
    const fetchData = async () => {  
      const response = await getNiftyData();  
      if (response.error) setError(response.error);  
      else setData(response);  
    };  
    fetchData();  

    // Auto-refresh every 60s  
    const interval = setInterval(fetchData, 60000);  
    return () => clearInterval(interval);  
  }, []);  

  return { data, error };  
};  