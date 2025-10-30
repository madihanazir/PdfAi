import React, { useState } from "react";
import axios from "axios";

function UploadPDF({ onFileUpload }) {
  const [message, setMessage] = useState("");

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";
      console.log("📡 Uploading to:", `${API_BASE_URL}/documents/upload`);

      const res = await axios.post(`${API_BASE_URL}/documents/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage("✅ File uploaded successfully!");
      if (onFileUpload) onFileUpload(res.data.document_id, file.name);
    } catch (error) {
      console.error("❌ Upload error:", error);
      setMessage(
        error.response?.data?.detail || "Failed to upload the file. Try again."
      );
    }
  };

  return (
    <div className="flex flex-col items-center gap-2">
      <label className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded text-white cursor-pointer">
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
          className="hidden"
        />
        Upload PDF
      </label>
      {message && <p className="text-sm text-gray-700">{message}</p>}
    </div>
  );
}

export default UploadPDF;
