# Run as a docker container using docker-compose up

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from querying import query_with_llama
from embeddings import generate_embeddings
from qdrant_client import QdrantClient
from llama_index.core import SimpleDirectoryReader


# Connect to your Qdrant instance
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

print("Checking Qdrant connection...")
if qdrant_url and qdrant_api_key:
    # Connect to your Qdrant cloud instance
    # streamlit run app.py
    print("Connecting to Qdrant cloud instance...")
    client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
    print("App running on:", qdrant_url)
else:
    # Connect locally
    # docker run -p 6333:6333 qdrant/qdrant
    # streamlit run app.py
    print("Connecting locally...")
    client = QdrantClient(host="localhost", port=6333)

# Streamlit interface
st.title("PwC Proposal Writer")

# Step 1: File Upload
st.header("Upload Your Documents")
uploaded_files = st.file_uploader("Upload .docx files", type="docx", accept_multiple_files=True)

if uploaded_files:
    # Save uploaded files to the documents directory
    documents_dir = "documents"
    os.makedirs(documents_dir, exist_ok=True)

    for uploaded_file in uploaded_files:
        with open(os.path.join(documents_dir, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())
    
    st.success(f"Uploaded {len(uploaded_files)} document(s) successfully!")

# Step 2: Process Uploaded Documents
st.header("Process and Embed Documents")
if st.button("Submit"):
    # Load documents from the folder using SimpleDirectoryReader
    loader = SimpleDirectoryReader(
        input_dir="documents",
        required_exts=".docx",
        recursive=True
    )
    documents = loader.load_data()  # Load documents from the directory
    
    # Generate embeddings for the loaded documents and index them
    index = generate_embeddings(documents, client)
    
    # Store the index in session state for querying later
    st.session_state['index'] = index
    st.success("Documents processed and embeddings generated ✅!")

# Step 3: Query
st.header("Enter your query")
query = st.text_area("Type your question", placeholder="E.g. Draft an opening slide for a new tech in deals proposal in the agriculture industry")

if st.button("Submit Query"):
    if query:
        if 'index' in st.session_state:
            index = st.session_state['index']
            response = query_with_llama(query, index)
            response_text = response.response if hasattr(response, 'response') else "No response found"
            st.write("Response:", response_text)
        else:
            st.error("Please process and embed documents before querying.")
    else:
        st.error("Please enter a query before submitting.")