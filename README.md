# RAG Application

A Retrieval-Augmented Generation (RAG) application built with Python, Streamlit, and Qdrant. This application allows you to process documents, generate embeddings, and perform semantic search queries using LLaMA Index and Qdrant vector store.

## 🚀 Features

- Document processing and embedding generation
- Semantic search capabilities
- Interactive web interface using Streamlit
- Flexible deployment options (local or cloud-based Qdrant)
- Docker containerization support

## 🛠️ Tech Stack

- **Frontend**: Streamlit (v1.41.1)
- **Vector Store**: Qdrant (client v1.13.2)
- **Embeddings & RAG**:
  - LlamaIndex (v0.12.12)
  - Ollama integration
  - HuggingFace embeddings
- **Document Processing**: docx2txt (v0.8)
- **ML/DL**:
  - PyTorch (v2.6.0)
  - Transformers (v4.48.1)
- **Environment**: Python-dotenv (v1.0.1)

## 📋 Prerequisites

- Python 3.x
- Docker and Docker Compose
- Qdrant (local or cloud instance)

## 🔧 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd pwc-rag-py
```

2. Set up environment variables:
   Create a `.env` file with:

```env
QDRANT_URL=your_qdrant_url    # Your Qdrant cloud instance URL (if using cloud deployment)
QDRANT_API_KEY=your_api_key   # Your Qdrant cloud API key (if using cloud deployment)
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Local Development

```bash
streamlit run app.py
```

### Using Docker Compose

1. Build the containers:

```bash
docker-compose build
```

2. Run the application:

```bash
docker-compose up
```

The application will be available at `http://localhost:8501`

## 🏗️ Project Structure

- `app.py` - Main Streamlit application
- `embeddings.py` - Embedding generation logic
- `querying.py` - Query processing and RAG implementation
- `documents/` - Directory for document storage
- `docker-compose.yml` - Docker Compose configuration
- `Dockerfile` - Docker container configuration
- `requirements.txt` - Python dependencies

## 🔄 Deployment Options

The application supports two deployment modes:

1. **Local Deployment**:

   - Uses a local Qdrant instance
   - Runs on `localhost:6333`
   - Suitable for development and testing

2. **Cloud Deployment**:
   - Uses Qdrant Cloud
   - Requires `QDRANT_URL` and `QDRANT_API_KEY`
   - Suitable for production use

## 🐳 Docker Support

The application is containerized using Docker and includes:

- Multi-service orchestration with Docker Compose
- Volume mounting for local development
- Environment variable management
- Automatic service dependency handling

## 📝 Usage

1. Start the application
2. Upload documents through the Streamlit interface
3. Generate embeddings for your documents
4. Perform semantic searches using natural language queries
5. View and analyze the results
