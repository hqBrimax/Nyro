import os
from typing import List
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

# Configurable chunk settings
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 100

def load_and_chunk(path: str, chunk_size: int = DEFAULT_CHUNK_SIZE, chunk_overlap: int = DEFAULT_CHUNK_OVERLAP) -> List[Document]:
    """
    Loads a file from the given path and splits it into smaller text chunks.

    Parameters:
    - path (str): Path to the input document (PDF, DOCX, TXT, etc.)
    - chunk_size (int): Max number of characters per chunk.
    - chunk_overlap (int): Number of overlapping characters between chunks.

    Returns:
    - List[Document]: A list of text chunks from the document.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Document not found: {path}")

    try:
        loader = UnstructuredFileLoader(path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        chunks = splitter.split_documents(documents)
        return chunks

    except Exception as e:
        raise RuntimeError(f"Failed to load and split document: {e}")
