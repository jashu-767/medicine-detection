import React from "react";

function ResultDisplay({ result }) {
  if (!result) return null;
  return (
    <div>
      <h3>Detected Medicine: {result.medicine}</h3>
      <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
    </div>
  );
}

export default ResultDisplay;
