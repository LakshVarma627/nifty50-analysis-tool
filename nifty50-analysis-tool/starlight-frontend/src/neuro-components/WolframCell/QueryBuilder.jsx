import React, { useState } from 'react';

const QueryBuilder = ({ onSubmit }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(query);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask Wolfram Alpha..."
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default QueryBuilder;
