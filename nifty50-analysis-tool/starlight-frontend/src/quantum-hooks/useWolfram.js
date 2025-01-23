import { useState, useEffect } from 'react';
import axios from 'axios';

const useWolfram = (query) => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!query) return;

    const fetchData = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await axios.get(`/api/wolfram?query=${encodeURIComponent(query)}`);
        setResult(response.data);
      } catch (err) {
        setError('Failed to fetch data from Wolfram API');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [query]);

  return { result, loading, error };
};

export default useWolfram;
