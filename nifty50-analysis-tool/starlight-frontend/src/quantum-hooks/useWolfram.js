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
      try {
        const response = await axios.post('/api/wolfram/query', { query });
        setResult(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [query]);

  return { result, loading, error };
};

export default useWolfram;
