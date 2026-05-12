import { useState } from "react"

function UploadBox() {

    const [selectedFile, setSelectedFile] = useState(null)

    const [dragging, setDragging] = useState(false)

    const handleFile = (file) => {

        if (file && file.type === "application/pdf") {

            setSelectedFile(file)

        } else {

            alert("Only PDF files allowed")
        }
    }

    const handleDrop = (event) => {

        event.preventDefault()

        setDragging(false)

        const file = event.dataTransfer.files[0]

        handleFile(file)
    }

    const uploadFile = async () => {

        if (!selectedFile) {

            alert("Please select a PDF")

            return
        }

        const formData = new FormData()

        formData.append(
            "file",
            selectedFile
        )

        try {

            const response = await fetch(

                "http://127.0.0.1:8000/upload/",

                {

                    method: "POST",

                    body: formData
                }
            )

            const data = await response.json()

            alert(data.message)

        } catch (error) {

            console.error(error)

            alert("Upload failed")
        }
    }

    return (

        <div
            onDragOver={(e) => {

                e.preventDefault()

                setDragging(true)
            }}

            onDragLeave={() => {

                setDragging(false)
            }}

            onDrop={handleDrop}

            className={`p-6 rounded-xl shadow-lg border-2 border-dashed transition-all ${
                dragging
                    ? "border-blue-400 bg-slate-700"
                    : "border-slate-600 bg-slate-800"
            }`}
        >

            <h2 className="text-xl font-bold mb-4">

                Upload Medical Report

            </h2>

            <p className="text-gray-400 mb-4">

                Drag & drop PDF here
                or choose file manually

            </p>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                    handleFile(
                        e.target.files[0]
                    )
                }
                className="mb-4"
            />

            <button
                onClick={uploadFile}
                className="bg-green-600 hover:bg-green-700 px-5 py-2 rounded-xl"
            >
                Upload PDF
            </button>

            {selectedFile && (

                <div className="mt-4 text-green-400">

                    {selectedFile.name}

                </div>
            )}

        </div>
    )
}

export default UploadBox