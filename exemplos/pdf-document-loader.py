# Exemplo de uso do PyPDFLoader para carregar um documento PDF
from langchain_community.document_loaders import PyPDFLoader

file_path = "./docs/Alan Turing – Wikipédia, a enciclopédia livre.pdf"

# caso dê problema no windows, use o caminho absoluto:
# import os
# file_path = os.path.abspath("./docs/Alan Turing – Wikipédia, a enciclopédia livre.pdf")
# ou digite o caminhho completo do arquivo ex. C:\Users\seu_usuario\docs\Alan Turing – Wikipédia, a enciclopédia livre.pdf

loader = PyPDFLoader(file_path)

docs = loader.load()

print("Conteúdo da página:\n" + docs[0].page_content[:700], end="...\n\n")

print("Metadados da página:", str(docs[0].metadata))
