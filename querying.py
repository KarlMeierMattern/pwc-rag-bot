from llama_index.core import PromptTemplate
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

# Set the local Ollama model (DeepSeek)
llm = Ollama(model="llama3.2", request_timeout=90.0)
Settings.llm = llm

# Define the prompt template
prompt_template = PromptTemplate(
    """
    You are a helpful assistant. Given the following context information, answer the question below.
    
    Context:
    {context_str}
    
    Question:
    {query_str}
    
    Answer:
    """
)

def query_with_llama(query, index):
    query_engine = index.as_query_engine(
        llm=llm,
        prompt_template=prompt_template
    )
    
    # Query the vector store
    response = query_engine.query(query)
    return response