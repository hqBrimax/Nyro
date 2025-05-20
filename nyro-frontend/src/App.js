import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  // Upload handler
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setUploadStatus("Uploading...");

    try {
      const res = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("Upload failed with server error.");
      }

      const data = await res.json();
      setUploadStatus(`Upload successful! Chunks: ${data.chunks || "N/A"}`);
      setFile(null); // Clear file input
    } catch (error) {
      setUploadStatus("Upload failed.");
      console.error(error);
    }
  };

  // Ask question handler
  const handleAsk = async () => {
    if (!question.trim()) {
      alert("Please type a question.");
      return;
    }

    setLoading(true);
    setAnswer("");

    try {
      const res = await fetch("http://127.0.0.1:8000/ask/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ q: question }),
      });

      if (!res.ok) {
        throw new Error("Failed to get answer from server.");
      }

      const data = await res.json();
      setAnswer(data.answer || "No answer returned.");
    } catch (error) {
      setAnswer("Failed to get answer.");
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20, fontFamily: "Arial, sans-serif" }}>
      <h1>Nyro AI Agent</h1>

      {/* Upload Section */}
      <section style={{ marginBottom: 30 }}>
        <h2>Upload Document</h2>
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          accept=".pdf,.txt,.docx"
        />
        <br />
        <button
          onClick={handleUpload}
          disabled={!file}
          style={{ marginTop: 10, padding: "6px 12px" }}
        >
          Upload
        </button>
        <p>{uploadStatus}</p>
      </section>

      <hr />

      {/* Question Section */}
      <section>
        <h2>Ask a Question</h2>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Type your question here"
          style={{ width: "100%", padding: 8, marginBottom: 10 }}
        />
        <br />
        <button onClick={handleAsk} disabled={loading} style={{ padding: "6px 12px" }}>
          {loading ? "Thinking..." : "Ask"}
        </button>
        <p><strong>Answer:</strong> {answer}</p>
      </section>
    </div>
  );
}

export default App;
