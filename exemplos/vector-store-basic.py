import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

# Configura embeddings Google
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

documents = [
    "gato",
    "cachorro",
    "avestruz",
]

vector_store = FAISS.from_texts(documents, embeddings)

query = "Qual animal é doméstico?"

query_embedding = embeddings.embed_query(query)
print("Embedding da consulta:", query_embedding[:5])

results = vector_store.similarity_search(query, k=2)

print("Pergunta:", query)
for i, doc in enumerate(results):
    print(f"Resultado {i+1}: {doc.page_content}")