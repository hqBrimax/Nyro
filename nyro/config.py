import os
from dotenv import load_dotenv

# === Load environment variables from .env ===
load_dotenv()

# === NYRO Agent Personality/Instructions ===
NYRO_INSTRUCTIONS = """
You are NYRO (Neural Yielded Reactive Operator), an elite AI assistant created by Nathan Oyewole.
You answer questions using your knowledge base with sharp, cinematic clarity. Be concise, only expand when needed.
"""

# === Model Configuration ===
DEFAULT_MODEL = "claude-3-opus-20240229"  # Change to claude-3-sonnet-20240229 if needed
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", DEFAULT_MODEL)

# === Anthropic API Key (required) ===
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise EnvironmentError("Missing required environment variable: ANTHROPIC_API_KEY")

# === Additional Optional Settings ===
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 800))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.3))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))  # For document chunking
OVERLAP = int(os.getenv("OVERLAP", 100))         # For overlapping chunks (if using)

# === Optional Debugging ===
DEBUG_MODE = os.getenv("DEBUG", "false").lower() in ("1", "true", "yes")

# === Export as settings object if needed (optional) ===
class Settings:
    model = CLAUDE_MODEL
    api_key = ANTHROPIC_API_KEY
    max_tokens = MAX_TOKENS
    temperature = TEMPERATURE
    chunk_size = CHUNK_SIZE
    chunk_overlap = OVERLAP
    instructions = NYRO_INSTRUCTIONS
    debug = DEBUG_MODE

settings = Settings()
