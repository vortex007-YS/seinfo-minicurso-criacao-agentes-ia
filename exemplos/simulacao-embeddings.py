from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import FAISS

# Configura embeddings fake
embeddings = FakeEmbeddings(size=1024)

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