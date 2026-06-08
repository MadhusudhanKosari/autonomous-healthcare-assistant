import "./ChatWindow.css";

import ReactMarkdown from "react-markdown";

function ChatBox({

  messages
}) {

  return (

    <div className="chat-window">

      {

        messages.length === 0 && (

          <div className="empty-chat">

            Ask healthcare questions or upload medical reports.

          </div>
        )
      }

      {

        messages.map((msg, index) => (

          <div
            key={index}
            className={

              msg.role === "user"

                ? "user-message"

                : "ai-message"
            }
          >

            <ReactMarkdown>

              {msg.content}

            </ReactMarkdown>

          </div>
        ))
      }

    </div>
  );
}

export default ChatBox;