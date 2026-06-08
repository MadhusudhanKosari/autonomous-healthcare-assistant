import "./Sidebar.css";

function Sidebar({
  chatHistory = [],
  onNewChat
}) {
  return (
    <div className="sidebar">

      <h2>Healthcare AI</h2>

      <button
        className="new-chat-btn"
        onClick={onNewChat}
      >
        + New Chat
      </button>

      <div className="uploaded-section">

        <h3>Recent Chats</h3>

        {
          chatHistory.length === 0
          ? (
            <p className="empty-text">
              No chats yet
            </p>
          )
          : (
            chatHistory.map(
              (chat, index) => (
                <div
                  key={index}
                  className="file-item"
                >
                  {chat}
                </div>
              )
            )
          )
        }

      </div>

    </div>
  );
}

export default Sidebar;