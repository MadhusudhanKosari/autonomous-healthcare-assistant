function ChatInput({

    message,

    setMessage,

    sendMessage,

    handleFileUpload

}) {

    return (

        <div className="p-5 border-t border-slate-800 bg-slate-900">

            <div className="flex items-center gap-3 bg-slate-800 border border-slate-700 rounded-2xl px-4 py-3 shadow-xl">

                <label
                    className="cursor-pointer text-2xl hover:scale-110 transition"
                >
                    📎

                    <input
                        type="file"
                        accept=".pdf"
                        hidden
                        onChange={handleFileUpload}
                    />

                </label>

                <textarea
                    className="flex-1 bg-transparent outline-none text-white resize-none text-lg"
                    rows="1"
                    placeholder="Message Healthcare AI..."
                    value={message}
                    onChange={(e) =>
                        setMessage(e.target.value)
                    }
                />

                <button
                    onClick={sendMessage}
                    className="bg-blue-600 hover:bg-blue-700 transition px-6 py-3 rounded-xl font-semibold"
                >
                    Send
                </button>

            </div>

        </div>
    )
}

export default ChatInput