function DocumentCard({

    filename

}) {

    return (

        <div className="bg-slate-800 border border-slate-700 rounded-2xl p-4">

            <div className="text-4xl mb-3">

                📄

            </div>

            <div className="text-sm text-gray-300 truncate">

                {filename}

            </div>

        </div>
    )
}

export default DocumentCard