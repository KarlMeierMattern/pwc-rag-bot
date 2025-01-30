from llama_index.core import PromptTemplate
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set up the Hugging Face model
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize the LLM
llm = HuggingFaceLLM(
    model=model,
    tokenizer=tokenizer,
    max_length=256,
    temperature=0.7
)
Settings.llm = llm

# Rest of your code remains the same
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