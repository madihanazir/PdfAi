import React, { useState } from "react";
import axios from "axios";

function AskQuestion({ documentId }) {
    const [question, setQuestion] = useState("");
    const [answers, setAnswers] = useState([]);

    const handleAskQuestion = async () => {
        if (!question.trim()) return;

        try {
            const res = await axios.post("http://127.0.0.1:8000/questions/ask", {
                document_id: documentId,
                question,
            });

            setAnswers((prev) => [
                ...prev,
                { question, answer: res.data.answer },
            ]);
            setQuestion("");
        } catch (error) {
            console.error("Failed to fetch the answer:", error);
        }
    };

    return (
        <div>
            <h2 className="text-lg font-semibold text-gray-800 mb-4">Ask Questions</h2>
            <input
                type="text"
                placeholder="Type your question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                className="w-full p-2 mb-4 bg-gray-100 border rounded focus:outline-none"
            />
            <button
                onClick={handleAskQuestion}
                className="bg-blue-500 px-4 py-2 rounded text-white"
            >
                Get Answer
            </button>

            <div className="mt-4">
                {answers.map((a, idx) => (
                    <div key={idx} className="mb-4">
                        <p className="font-bold">Q: {a.question}</p>
                        <p className="text-green-600">A: {a.answer}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default AskQuestion;
