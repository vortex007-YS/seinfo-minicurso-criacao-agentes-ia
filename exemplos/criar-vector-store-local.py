import os
os.environ["USER_AGENT"] = "langchain-agent" # usei essa variável de ambiente para evitar warning da requisição

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

# Configura embeddings Google
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

DB_NAME = "faiss/minecraft_redstone"
loader = PyPDFLoader("docs/Circuitos de redstone.pdf")

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, separator="\n")
docs = loader.load_and_split(text_splitter=splitter)

print(len(docs), "documentos carregados.")

print("Criando novo vetor store FAISS...")
db = FAISS.from_documents(docs, embeddings)
db.save_local(DB_NAME)
print("Vetor store FAISS salvo em:", DB_NAME + "/index.faiss")