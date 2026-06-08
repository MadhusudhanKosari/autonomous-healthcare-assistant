import "./App.css";

import {
  useState
} from "react";

import Sidebar from "./components/Sidebar";
import ChatBox from "./components/ChatBox";
import ChatInput from "./components/ChatInput";

import {
  uploadPDF,
  startNewChat
} from "./services/api";

function App() {

  const [messages, setMessages] =
    useState([]);

  const [chatHistory, setChatHistory] =
    useState([]);

  const handleUpload = async (
    file
  ) => {

    try {

      await uploadPDF(file);

      alert(
        "PDF uploaded successfully"
      );

    } catch (error) {

      console.error(error);

      alert(
        "Upload failed"
      );
    }
  };

  const handleNewChat = async () => {

    try {

      await startNewChat();

      setMessages([]);

      setChatHistory([]);

    } catch (error) {

      console.error(error);
    }
  };

  return (

    <div className="app">

      <Sidebar
        chatHistory={chatHistory}
        onNewChat={handleNewChat}
      />

      <div className="main-content">

        <div className="header">

          <h1>
            Autonomous Healthcare Assistant
          </h1>

        </div>

        <ChatBox
          messages={messages}
        />

        <ChatInput
          messages={messages}
          setMessages={setMessages}
          setChatHistory={setChatHistory}
          chatHistory={chatHistory}
          onUpload={handleUpload}
        />

      </div>

    </div>
  );
}

export default App;