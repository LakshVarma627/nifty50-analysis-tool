import React, { useState } from 'react';
import QueryBuilder from '../../neuro-components/WolframCell/QueryBuilder';
import ResultCanvas from '../../neuro-components/WolframCell/ResultCanvas';
import useWolfram from '../../quantum-hooks/useWolfram';

const QuantumAnalysis = () => {
  const [query, setQuery] = useState('');
  const { result, loading, error } = useWolfram(query);

  const handleQuerySubmit = (newQuery) => {
    setQuery(newQuery);
  };

  return (
    <div>
      <h1>Quantum Analysis</h1>
      <QueryBuilder onSubmit={handleQuerySubmit} />
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
      {result && <ResultCanvas result={result} />}
    </div>
  );
};

export default QuantumAnalysis;
