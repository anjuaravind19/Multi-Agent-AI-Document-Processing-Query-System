🧠 Multi-Agent AI Document Processing & Query System

This project is a full-stack application for uploading and analyzing client documents using a multi-agent AI orchestration framework. Built with Streamlit, FastAPI, and LangChain, it leverages LLMs from Groq and Ollama for fast, contextual document-based query resolution.
🚀 Features

    📄 Streamlit-based document upload form

    🗃️ MongoDB integration for secure document storage

    🧠 Multi-agent AI orchestration using LangChain

    🔍 Intelligent document retrieval via vector embeddings (FAISS)

    🤖 LLM-backed bot using Groq’s and Ollama’s LLaMA3 models

    🌐 REST API backend built with FastAPI & Pydantic

    🧰 Tooling for document-based and general knowledge queries

📁 Project Structure


.
├── backend/
│   └── main.py                     # FastAPI server and API endpoints
├── forms/
│   ├── application_form.py         # Streamlit document upload form
│   ├── db/
│   │   └── mongoclient.py          # MongoDB client setup for form submissions
│   └── utils/
│       └── file_utils.py              # Utility functions for handling file uploads
├── frontend/
│   └── app.py                      # Streamlit + React-based frontend UI
├── shared/
│   ├── agent.py                    # Multi-agent AI orchestration tools
│   └── vector.py                   # Vectorization logic using FAISS and Ollama
├── uploads/                        # Stores locally uploaded files
├── .env                            # Environment variable definitions
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation


🔧 Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Install Required Dependencies

pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file in the root directory with the following:

GROQ_API_KEY=your_groq_key
LANGCHAIN_API_KEY=your_langchain_key
LANGCHAIN_PROJECT=your_project_name
MONGO_URI=your_mongo_connection_string
MONGO_DB=your_db_name

Set up your MongoDB user and database manually or via mongosh.
4. Start the Upload Form

streamlit run forms/application_form.py

You can now upload:

    Emirates ID

    Credit Report

    Bank Statements

    Other documents

These are saved to both MongoDB and a local uploads/ directory.
5. Install Ollama and Pull Model

Install Ollama and pull the LLaMA3 model:

ollama pull llama3

🧠 Backend & AI Orchestration
6. Backend API

    Located at backend/main.py

    Built with FastAPI and Pydantic

    Contains endpoints for data interaction

    Implements LangChain’s multi-agent system

7. Document Vectorization

shared/vector.py:

    Converts documents to embeddings

    Uses FAISS as vector store

    Employs Ollama embeddings

8. AI Agent Tools

shared/agent.py:

    create_retriever_tool to fetch data from uploaded documents

    Wrapper for general queries (e.g., Arxiv search)

    Tools integrated into LangChain agent

9. LLM Integration

    Uses Groq for fast LLM responses (15x speed boost)

    LLaMA3 model used for both Ollama and Groq backends

⚙️ Running the Application
Open Two Terminals:
Terminal 1: Start FastAPI Backend

uvicorn backend.main:app --reload --port 8080

Terminal 2: Start Frontend

streamlit run frontend/app.py

🤖 How It Works

    Users upload documents via the form.

    Files are saved in MongoDB and locally.

    FastAPI serves as a backend for document queries.

    LangChain manages the orchestration between:

        Retriever tools (for document Q&A)

        General tools (e.g., Arxiv, knowledge)

        LLMs (Groq, Ollama)

    User queries are intelligently routed and answered by the AI agent.

📌 Notes

    Ensure MongoDB is properly configured and user has correct permissions.

    Ollama should be installed and LLaMA3 model available.

    Make sure all .env values are correctly filled.

    You can customize LangChain agents and tools in shared/agent.py.


Currently, the project uses dummy documents — including a bank statement, Emirates ID, and a credit report — which were sourced from publicly available internet samples. These are used purely for demonstration and development purposes.

In a real-world scenario, replacing these with authentic and representative documents will significantly enhance the project. With more accurate data:

    The agent AI orchestration can be improved for better context understanding.

    More functions and tools can be added and tested.

    Overall accuracy, robustness, and scalability of the system will be increased.

This lays the groundwork for building a much more capable and production-ready intelligent document processing system.

📬 Contact

For support, reach out via [anjuaravind02@gmail.com] or create an issue.
