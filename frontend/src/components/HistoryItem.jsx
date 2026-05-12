function HistoryItem({

    title,

    onClick

}) {

    return (

        <div

            onClick={onClick}

            className="p-4 rounded-2xl bg-slate-900/70 hover:bg-slate-800 transition cursor-pointer text-gray-300 truncate border border-slate-800"

        >

            {title}

        </div>
    )
}

export default HistoryItem