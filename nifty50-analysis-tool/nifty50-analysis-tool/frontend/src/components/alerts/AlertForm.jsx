import { useState } from 'react';
import api from '../../services/api';

export default function AlertForm() {
  const [price, setPrice] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post('/alerts/', { target_price: price });
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
    </form>
  );
}