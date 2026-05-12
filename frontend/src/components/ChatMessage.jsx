import ReactMarkdown from "react-markdown"

import { motion } from "framer-motion"

function ChatMessage({

    sender,
    text

}) {

    const isUser = sender === "user"

    return (

        <motion.div

            initial={{
                opacity: 0,
                y: 10
            }}

            animate={{
                opacity: 1,
                y: 0
            }}

            transition={{
                duration: 0.25
            }}

            className={`flex ${
                isUser
                    ? "justify-end"
                    : "justify-start"
            }`}
        >

            <div

                className={`max-w-3xl px-5 py-4 rounded-3xl shadow-lg leading-8 backdrop-blur-md border ${
                    isUser
                        ? "bg-blue-600/90 border-blue-500"
                        : "bg-slate-800/90 border-slate-700"
                }`}
            >

                <ReactMarkdown>

                    {text}

                </ReactMarkdown>

            </div>

        </motion.div>
    )
}

export default ChatMessage