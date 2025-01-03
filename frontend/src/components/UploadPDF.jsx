import React, { useState } from "react";
import axios from "axios";

function UploadPDF({ onFileUpload }) {
    const [message, setMessage] = useState("");

    const handleFileChange = async (event) => {
        const file = event.target.files[0];
        if (file) {
            const formData = new FormData();
            formData.append("file", file);

            try {
                const res = await axios.post("http://127.0.0.1:8000/documents/upload", formData);
                setMessage("File uploaded successfully!");
                onFileUpload(res.data.document_id, file.name);
            } catch (error) {
                setMessage("Failed to upload the file.");
                console.error(error);
            }
        }
    };

    return (
        <label className="bg-green-500 px-4 py-2 rounded cursor-pointer text-white">
            <input
                type="file"
                accept="application/pdf"
                onChange={handleFileChange}
                className="hidden"
            />
            Upload PDF
        </label>
    );
}

export default UploadPDF;
