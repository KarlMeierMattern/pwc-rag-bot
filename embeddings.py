from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama

# Load Hugging Face tokenizer and model
# model_embed_local = Ollama(model="nomic-embed-text", request_timeout=90.0)
model_name = "nomic-ai/modernbert-embed-base"  # You can change this to another model
cache_folder = "cache/models"

# Initialize the embedding model
embed_model = HuggingFaceEmbedding(
    model_name=model_name,
    cache_folder=cache_folder,
    trust_remote_code=True
)

def generate_embeddings(documents, client):
    # Define the collection name
    collection_name = "chat_with_docs"

    # Initialize the Qdrant vector store
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name
    )
    
    # Set up the storage context with Qdrant
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Generate the index (no manual upsert required)
    index = VectorStoreIndex(
        documents,
        storage_context=storage_context,
        embed_model=embed_model,
    )
    
    return index