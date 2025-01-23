import { useState } from 'react';
import api from '../../services/api';

export default function AlertForm() {
  const [price, setPrice] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/alerts/', { target_price: price });
    } catch (err) {
      setError('Failed to set alert. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="number" 
        value={price}
        onChange={(e) => setPrice(e.target.value)}
        placeholder="Enter target price"
      />
      <button type="submit">Set Alert</button>
      {error && <p>{error}</p>}
    </form>
  );
}
