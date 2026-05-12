import {

    useEffect,
    useRef,
    useState

} from "react"

import { v4 as uuidv4 } from "uuid"

import ChatMessage from "./ChatMessage"

import ChatInput from "./ChatInput"

function ChatBox({

    messages,
    setMessages,

    sessionId,
    setSessionId,

    saveCurrentChat,
    documents,
setDocuments
}) {

    const [message, setMessage] = useState("")

    const [loading, setLoading] = useState(false)

    const messagesEndRef = useRef(null)

    const scrollToBottom = () => {

        messagesEndRef.current?.scrollIntoView({

            behavior: "smooth"
        })
    }

    useEffect(() => {

        scrollToBottom()

    }, [messages])

    const handleFileUpload = async (event) => {

        const file = event.target.files[0]

        if (!file) return

        const formData = new FormData()

        formData.append("file", file)

        try {

            await fetch(

                "http://127.0.0.1:8000/upload/",

                {

                    method: "POST",

                    body: formData
                }
            )

            alert("PDF uploaded successfully")
            setDocuments((prev) => [

    ...prev,

    file.name
])

        } catch (error) {

            console.error(error)

            alert("Upload failed")
        }
    }

    const sendMessage = async () => {

        if (!message.trim()) return

        const userMessage = {

            sender: "user",

            text: message
        }

        const updatedMessages = [

            ...messages,

            userMessage
        ]

        setMessages(updatedMessages)

        setLoading(true)

        const aiMessage = {

            sender: "ai",

            text: ""
        }

        setMessages((prev) => [

            ...prev,

            aiMessage
        ])

        try {

            const response = await fetch(

                "http://127.0.0.1:8000/stream-chat/",

                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({

                        query: message
                    })
                }
            )

            const reader = response.body.getReader()

            const decoder = new TextDecoder()

            let done = false

            let accumulatedText = ""

            while (!done) {

                const result = await reader.read()

                done = result.done

                const chunk = decoder.decode(

                    result.value || new Uint8Array()
                )

                accumulatedText += chunk

                setMessages((prev) => {

                    const updated = [...prev]

                    updated[updated.length - 1] = {

                        sender: "ai",

                        text: accumulatedText
                    }

                    return updated
                })
            }

            saveCurrentChat(
                updatedMessages,
                message
            )

        } catch (error) {

            console.error(error)

        } finally {

            setLoading(false)

            setMessage("")
        }
    }

    return (

        <div className="flex flex-col h-full">

            <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">

                {messages.map((msg, index) => (

                    <ChatMessage
                        key={index}
                        sender={msg.sender}
                        text={msg.text}
                    />
                ))}

                {loading && (

    <div className="flex items-center gap-2 text-gray-400 px-2">

        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>

        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-100"></div>

        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-200"></div>

    </div>
)}

                <div ref={messagesEndRef} />

            </div>

            <ChatInput
                message={message}
                setMessage={setMessage}
                sendMessage={sendMessage}
                handleFileUpload={handleFileUpload}
            />

        </div>
    )
}

export default ChatBox