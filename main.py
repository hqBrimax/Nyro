from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from nyro.loader import load_and_chunk
from nyro.vector_store import create_vector_store, save_vector_store
from nyro.agent import ask_nyro

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_doc(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)

    chunks = load_and_chunk(file.filename)
    vectorstore = create_vector_store(chunks)
    save_vector_store(vectorstore)
    return {"status": "uploaded", "chunks": len(chunks)}

@app.post("/ask/")
async def ask_question(q: str):
    answer = ask_nyro(q)
    return {"answer": answer}

@app.get("/")
async def root():
    return {"message": "Nyro AI Agent is running"}
