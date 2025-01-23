import { useEffect, useState } from 'react';
import { fetchStockData } from '../services/api';

export const useStockData = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchStockData().then(data => setData(data));
  }, []);

  return data;
};