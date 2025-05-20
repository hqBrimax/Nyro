import anthropic
from .vector_store import load_vector_store
from .utils import format_claude_prompt
from .config import CLAUDE_MODEL, ANTHROPIC_API_KEY, NYRO_INSTRUCTIONS

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def ask_nyro(question: str) -> str:
    """
    Uses Claude to answer a question based on context from a vector store.
    
    Args:
        question (str): The user question.
    
    Returns:
        str: The model's response.
    """

    # Load the vector DB and get relevant documents
    db = load_vector_store()
    retriever = db.as_retriever()
    docs = retriever.get_relevant_documents(question)
    
    if not docs:
        return "No relevant context found."

    # Use the top 4 documents for context
    context = "\n\n".join(doc.page_content for doc in docs[:4])

    # Format Claude-compatible prompt
    prompt = format_claude_prompt(context, question, NYRO_INSTRUCTIONS)

    # Send the prompt to Claude
    try:
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=800,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text  # Claude v1.2-style format
    except Exception as e:
        print(f"[ERROR] Claude API call failed: {e}")
        return "Error: Failed to get a response from Claude."
