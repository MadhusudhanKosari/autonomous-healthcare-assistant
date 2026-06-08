import { useState } from "react";
import "./ChatInput.css";
import { sendMessage } from "../services/api";

function ChatInput({
  setMessages,
  messages,
  onUpload,
  setChatHistory
}) {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const currentInput = input;

    const userMessage = {
      role: "user",
      content: currentInput
    };

    setMessages((prev) => [
      ...prev,
      userMessage
    ]);

    // Add to recent chats
    if (setChatHistory) {
      setChatHistory((prev) => [
        currentInput,
        ...prev.filter(
          (chat) => chat !== currentInput
        )
      ].slice(0, 20));
    }

    setInput("");

    try {
      setLoading(true);

      const response = await sendMessage(
        currentInput
      );

      const aiMessage = {
        role: "assistant",
        content: response.data
      };

      setMessages((prev) => [
        ...prev,
        aiMessage
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Error generating response."
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      onUpload(file);
    }
  };

  const handleKeyDown = (e) => {
    if (
      e.key === "Enter" &&
      !e.shiftKey
    ) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-input-container">

      <textarea
        value={input}
        onChange={(e) =>
          setInput(e.target.value)
        }
        onKeyDown={handleKeyDown}
        placeholder="Ask healthcare questions..."
      />

      <label className="upload-btn">
        📎

        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          hidden
        />
      </label>

      <button
        onClick={handleSend}
        disabled={loading}
      >
        {loading ? "..." : "Send"}
      </button>

    </div>
  );
}

export default ChatInput;