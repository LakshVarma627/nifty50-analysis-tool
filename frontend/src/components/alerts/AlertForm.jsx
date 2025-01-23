import { useState } from 'react';

export default function AlertForm() {
  const [alert, setAlert] = useState({
    price: '',
    condition: 'above',
    asset: 'NIFTY50'
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Alert set:', alert);
  };

  return (
    <form onSubmit={handleSubmit} className="alert-form">
      <div className="form-group">
        <label>Alert when NIFTY50 is</label>
        <select 
          value={alert.condition}
          onChange={(e) => setAlert({...alert, condition: e.target.value})}
        >
          <option value="above">Above</option>
          <option value="below">Below</option>
        </select>
        <input
          type="number"
          value={alert.price}
          onChange={(e) => setAlert({...alert, price: e.target.value})}
          placeholder="Enter price"
        />
      </div>
      <button type="submit">Set Alert</button>
    </form>
  );
}