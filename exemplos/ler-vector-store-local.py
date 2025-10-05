import os
os.environ["USER_AGENT"] = "langchain-agent" # usei essa variável de ambiente para evitar warning da requisição

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

# Configura embeddings Google
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


DB_NAME = "faiss/minecraft_redstone"
if os.path.exists(f"{DB_NAME}/index.faiss"):
    db = FAISS.load_local(DB_NAME, embeddings, allow_dangerous_deserialization=True)
    print("Carregado com sucesso")

pergunta = "Como liga um circuito de redstone?"
docs_retornados = db.similarity_search(pergunta, k=5)

for doc in docs_retornados:
    print(doc.page_content)
    print("----")
