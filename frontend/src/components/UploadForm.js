import React, { useState } from "react";

const UploadForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);

  const detectMedicine = async () => {
    if (!selectedFile) {
      alert("Please select an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://localhost:8000/predict/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Prediction failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Network error:", error);
      alert("Network error. Make sure the ML server is running.");
    }
  };

  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      minHeight: "100vh",
      backgroundColor: "#f5f7fa",
      fontFamily: "Segoe UI, sans-serif"
    }}>
      <div style={{
        backgroundColor: "#ffffff",
        padding: "30px",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)",
        width: "100%",
        maxWidth: "400px",
        textAlign: "center"
      }}>
        <h2 style={{ color: "#333", marginBottom: "20px" }}>Medicine Detection App</h2>
        <input
          type="file"
          onChange={(e) => setSelectedFile(e.target.files[0])}
          style={{
            marginBottom: "15px",
            padding: "8px",
            borderRadius: "6px",
            border: "1px solid #ccc",
            width: "100%"
          }}
        />
        <button
          onClick={detectMedicine}
          style={{
            backgroundColor: "#4a90e2",
            color: "#fff",
            padding: "10px 20px",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            fontWeight: "bold"
          }}
        >
          Detect Medicine
        </button>

        {result && (
          <div style={{
            marginTop: "25px",
            backgroundColor: "#f0f4f8",
            padding: "15px",
            borderRadius: "8px"
          }}>
            <h3 style={{ marginBottom: "10px", color: "#2c3e50" }}>Prediction Result</h3>
            <p><strong>Medicine:</strong> {result.medicine}</p>
            <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(2)}%</p>
            <p><strong>Usage:</strong> {result.usage}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default UploadForm;
