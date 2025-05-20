def format_claude_prompt(context: str, question: str, instructions: str) -> str:
    """
    Formats a Claude-compatible prompt using system instructions, relevant context, and the user's question.

    Parameters:
    - context (str): The retrieved document text (chunks).
    - question (str): The user's query.
    - instructions (str): Agent persona and guidelines.

    Returns:
    - str: The full Claude prompt.
    """
    # Fallback if any parameter is empty
    context = context.strip() if context else "No relevant context available."
    question = question.strip() if question else "No question provided."
    instructions = instructions.strip() if instructions else "You are a helpful assistant."

    return (
        f"\n\nHuman: {instructions}\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        f"Assistant:"
    )
