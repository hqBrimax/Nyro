from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Default values
DEFAULT_EMBED_MODEL = "all-MiniLM-L6-v2"
DEFAULT_STORE_PATH = "nyro_index"

def get_embeddings(model_name: str = DEFAULT_EMBED_MODEL):
    """
    Load a HuggingFace embedding model.

    Args:
        model_name (str): The name of the embedding model to use.

    Returns:
        HuggingFaceEmbeddings: An instance of the embeddings class.
    """
    return HuggingFaceEmbeddings(model_name=model_name)

def create_vector_store(chunks, model_name: str = DEFAULT_EMBED_MODEL):
    """
    Create a FAISS vector store from document chunks.

    Args:
        chunks (List[Document]): The text/document chunks.
        model_name (str): HuggingFace model name for embeddings.

    Returns:
        FAISS: The vector store.
    """
    embeddings = get_embeddings(model_name)
    return FAISS.from_documents(chunks, embeddings)

def save_vector_store(db: FAISS, path: str = DEFAULT_STORE_PATH):
    """
    Save the FAISS vector store to disk.

    Args:
        db (FAISS): The vector store.
        path (str): Directory path to save the index.
    """
    db.save_local(path)

def load_vector_store(path: str = DEFAULT_STORE_PATH, model_name: str = DEFAULT_EMBED_MODEL):
    """
    Load a FAISS vector store from disk.

    Args:
        path (str): Directory path of the saved index.
        model_name (str): HuggingFace model name for embeddings.

    Returns:
        FAISS: The loaded vector store.
    """
    embeddings = get_embeddings(model_name)
    return FAISS.load_local(path, embeddings)
