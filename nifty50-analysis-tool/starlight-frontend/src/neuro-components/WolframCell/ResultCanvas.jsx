import React from 'react';

const ResultCanvas = ({ result }) => {
  return (
    <div>
      <h3>Wolfram Alpha Result</h3>
      {result.pods.map((pod, index) => (
        <div key={index}>
          <h4>{pod.title}</h4>
          <p>{pod.content}</p>
        </div>
      ))}
    </div>
  );
};

export default ResultCanvas;
