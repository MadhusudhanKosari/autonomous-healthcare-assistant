🩺 Autonomous Healthcare Assistant  

An AI-powered healthcare assistant built with FastAPI, React, LangChain, LangGraph, ChromaDB, and Groq LLMs that can understand medical reports, answer healthcare-related queries, perform intelligent document retrieval (RAG), maintain conversational memory, and provide AI-assisted healthcare guidance.

🚀 Project Vision

The goal of this project is to build a production-grade autonomous healthcare AI system that combines:

Conversational AI
Medical document understanding
RAG (Retrieval-Augmented Generation)
AI agents
Conversational memory
OCR
Medical recommendation workflows
Modern AI UI
Scalable backend architecture

This project is designed as a real-world AI Engineering portfolio project focused on:

AI Engineering
Backend Engineering
Full Stack Development
LLM Application Development
Production Deployment
🌟 Unique Selling Points (USP)

✅ AI-powered medical report analysis
✅ Retrieval-Augmented Generation (RAG) pipeline
✅ Conversational memory support
✅ OCR-based scanned PDF understanding
✅ Modular AI agent architecture
✅ Modern healthcare assistant UI
✅ ChromaDB vector database integration
✅ Groq-powered ultra-fast LLM responses
✅ Scalable FastAPI backend
✅ Production-ready architecture design
✅ Beginner-friendly but industry-standard structure

🧠 Core Features
📄 Medical PDF Understanding
Upload healthcare reports
Extract text from PDFs
OCR fallback for scanned reports
Intelligent chunking pipeline
🔍 RAG Pipeline
Semantic document chunking
Embedding generation
ChromaDB vector storage
Context retrieval
LLM-grounded responses
🤖 Conversational AI
Healthcare-focused AI assistant
Context-aware conversations
Memory-enabled interactions
Multi-turn chat support
🧠 AI Agents & Workflow
Retrieval agent
Recommendation agent
Medical response orchestration
LangGraph workflow integration
🧾 Recommendation System

Provides:

Lifestyle suggestions
Diet recommendations
Hydration guidance
Exercise recommendations
💬 Conversational Memory
Stores previous messages
Maintains context across conversation
Session-based interactions
🎨 Modern Frontend
Responsive UI
Chat-style interaction
Upload interface
Chat history sidebar
Clean healthcare-themed design
🏗️ Tech Stack
Backend
Python
FastAPI
LangChain
LangGraph
ChromaDB
SQLite
Groq API
Frontend
React
Vite
Axios
Modern CSS
AI/ML
Retrieval-Augmented Generation (RAG)
Embeddings
Vector Search
OCR
Conversational AI
📂 Project Structure
autonomous-healthcare-assistant/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── rag/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── chroma_db/
│   ├── uploads/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── docker/
├── docs/
├── README.md
└── .gitignore
⚙️ Local Setup Guide
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/autonomous-healthcare-assistant.git
cd autonomous-healthcare-assistant
2️⃣ Backend Setup
Navigate to backend
cd backend
Create Virtual Environment
Windows
python -m venv venv
Activate Environment
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment Variables

Create file:

backend/.env

Add:

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama3-8b-8192
🔑 Get Free API Key
Groq API

Get FREE API key from:

Groq Console

4️⃣ Run Backend
uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000
5️⃣ Frontend Setup

Open new terminal.

cd frontend
Install Frontend Dependencies
npm install
Run Frontend
npm run dev

Frontend runs on:

http://localhost:5173
🧪 Testing the Project
Test Chat API

Open:

http://127.0.0.1:8000/docs

Use Swagger UI to:

upload PDFs
test chat endpoint
test workflows
📄 Uploading Medical Reports

Supported:

PDF reports
Medical documents
Lab reports

The system:

extracts text
chunks content
stores embeddings
performs semantic retrieval
generates AI-assisted responses
🛡️ Security Notes

❌ Never upload .env to GitHub
❌ Never expose API keys publicly
✅ Use environment variables
✅ Use .gitignore properly

🚧 Current Development Status
✅ Implemented
FastAPI backend
React frontend
RAG pipeline
ChromaDB integration
PDF upload
Conversational AI
Chat memory
OCR fallback
AI workflow system
🔄 In Progress
Production deployment
Streaming responses
Authentication
Long-term memory
Multi-agent orchestration improvements
Cloud deployment optimization
🔮 Future Improvements
Voice assistant
Doctor recommendation system
Medical image understanding
Real-time notifications
Appointment scheduling
Cloud vector DB
Docker deployment
Kubernetes scaling
Monitoring dashboard
📸 Screenshots

Add screenshots of:

Home page
Chat UI
Upload workflow
AI responses
Chat history sidebar
🧠 AI Engineering Concepts Used
RAG (Retrieval-Augmented Generation)
Vector Databases
Embeddings
Semantic Search
LLM Orchestration
AI Agents
Prompt Engineering
Conversational Memory
OCR Pipelines
FastAPI Architecture
💼 Resume-Worthy Highlights

This project demonstrates:

✅ AI Engineering
✅ Full Stack Development
✅ LLM Application Development
✅ Backend API Design
✅ Vector Database Integration
✅ Retrieval Systems
✅ AI Workflow Engineering
✅ Production Architecture

🎯 Ideal For
AI Engineering portfolios
Final year projects
Hackathons
Resume projects
LLM application showcases
Healthcare AI demonstrations
🤝 Contributing

Contributions are welcome.

Steps:

Fork repository
Create feature branch
Commit changes
Open pull request
📜 License

This project is intended for educational and research purposes.

⚠️ Disclaimer

This AI assistant does NOT replace professional medical advice.

Always consult licensed healthcare professionals for medical decisions.

👨‍💻 Author

Developed by YOUR_NAME

AI Engineering & Full Stack AI Project

⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

🔥 Final Note

This project is built as a real-world AI engineering system combining:

modern LLM workflows,
healthcare AI concepts,
retrieval systems,
scalable backend architecture,
and production-grade engineering practices.

It represents a strong foundation for building next-generation AI healthcare systems.
