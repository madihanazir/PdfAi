import React, { useState } from "react";
import UploadPDF from "./components/UploadPDF";
import AskQuestion from "./components/AskQuestion";

function App() {
    const [documentId, setDocumentId] = useState(null);
    const [uploadedFileName, setUploadedFileName] = useState("");

    const handleFileUpload = (docId, fileName) => {
        setDocumentId(docId);
        setUploadedFileName(fileName);
    };

    return (
        <div className="min-h-screen bg-gray-100 flex flex-col">
            {/* Header */}
            <header className="bg-gray-800 w-full p-4 flex items-center justify-between">
                <div className="text-xl font-bold text-white">
                    <span className="text-green-400">ai</span> tutor
                    
                </div>
                <UploadPDF onFileUpload={handleFileUpload} />
            </header>

            {/* Content */}
            <div className="flex flex-col lg:flex-row w-full max-w-7xl mx-auto mt-8 gap-4 p-4">
                {/* Left Section */}
                <div className="flex-1 bg-white p-4 rounded-lg shadow">
                    <AskQuestion documentId={documentId} />
                </div>

                {/* Right Section */}
                <div className="w-full lg:w-1/3 bg-gray-50 p-4 rounded-lg shadow">
                    <h2 className="text-lg font-semibold text-gray-800 mb-4">Uploaded PDF</h2>
                    {uploadedFileName ? (
                        <p className="text-green-500">{uploadedFileName}</p>
                    ) : (
                        <p className="text-gray-500">No file uploaded</p>
                    )}
                </div>
            </div>
        </div>
    );
}

export default App;
