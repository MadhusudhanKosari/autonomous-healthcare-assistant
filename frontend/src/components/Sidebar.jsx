import HistoryItem from "./HistoryItem"

function Sidebar({

    startNewChat,

    chatHistory,

    loadChat,
    documents

}) {

    return (

        <div className="w-72 bg-black/40 backdrop-blur-xl border-r border-slate-800 flex flex-col">

            <div className="p-5">

                <h1 className="text-3xl font-bold mb-8">

                    Healthcare AI

                </h1>

                <button
                    onClick={startNewChat}
                    className="w-full bg-blue-600 hover:bg-blue-700 transition py-3 rounded-2xl mb-8 font-semibold shadow-lg"
                >
                    + New Chat
                </button>

                <div className="space-y-2 overflow-y-auto max-h-[75vh]">

                    {chatHistory.map((chat, index) => (

                        <HistoryItem
                            key={index}
                            title={chat.title}
                            onClick={() =>
                                loadChat(chat)
                            }
                        />
                    ))}
                    <div className="mt-8">

    <h2 className="text-lg font-semibold mb-3">

        Documents

    </h2>

    <div className="space-y-2">

        {documents.map((doc, index) => (

            <div
                key={index}
                className="bg-slate-900 p-3 rounded-xl text-sm truncate"
            >

                📄 {doc}

            </div>
        ))}

    </div>

</div>
                </div>

            </div>

        </div>
    )
}

export default Sidebar