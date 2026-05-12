import {

  useEffect,
  useState

} from "react"

import { v4 as uuidv4 } from "uuid"

import Sidebar from "./components/Sidebar"

import ChatBox from "./components/ChatBox"

function App() {

  const [messages, setMessages] = useState([])
  const [documents, setDocuments] = useState([])

  const [sessionId, setSessionId] = useState(

    uuidv4()
  )

  const [chatHistory, setChatHistory] = useState([])


  // LOAD SAVED HISTORY
  useEffect(() => {

    const savedHistory = localStorage.getItem(

      "healthcare_chat_history"
    )

    if (savedHistory) {

      setChatHistory(

        JSON.parse(savedHistory)
      )
    }

  }, [])


  // SAVE HISTORY AUTOMATICALLY
  useEffect(() => {

    localStorage.setItem(

      "healthcare_chat_history",

      JSON.stringify(chatHistory)
    )

  }, [chatHistory])


  const startNewChat = () => {

    setMessages([])

    setSessionId(uuidv4())
  }


  const saveCurrentChat = (

    updatedMessages,

    title

  ) => {

    if (!title) return

    const newChat = {

      id: sessionId,

      title: title.slice(0, 30),

      messages: updatedMessages
    }

    setChatHistory((prev) => {

      const filtered = prev.filter(

        (chat) => chat.id !== sessionId
      )

      return [

        newChat,

        ...filtered
      ]
    })
  }


  const loadChat = (chat) => {

    setMessages(chat.messages)

    setSessionId(chat.id)
  }


  return (

    <div className="flex flex-col md:flex-row h-screen">

      <Sidebar
        startNewChat={startNewChat}
        chatHistory={chatHistory}
        loadChat={loadChat}
        documents={documents}
      />

      <div className="flex-1 flex flex-col">

        <div className="p-6 border-b border-slate-800">

          <h1 className="text-4xl font-bold text-center">

            Autonomous Healthcare Assistant

          </h1>

        </div>

        <div className="flex-1 overflow-hidden">

          <ChatBox
            messages={messages}
            setMessages={setMessages}
            sessionId={sessionId}
            setSessionId={setSessionId}
            saveCurrentChat={saveCurrentChat}
            documents={documents}
            setDocuments={setDocuments}
          />

        </div>

      </div>

    </div>
  )
}

export default App