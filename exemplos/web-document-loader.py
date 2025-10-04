# Exemplo de uso do WebBaseLoader
import os
os.environ["USER_AGENT"] = "langchain-agent" # usei essa variável de ambiente para evitar warning da requisição
from langchain_community.document_loaders import WebBaseLoader # requires beatifulsoup4

loader = WebBaseLoader("https://pt.minecraft.wiki/w/Circuitos_de_redstone")

docs = loader.load()

print("Conteúdo da página:\n" + docs[0].page_content[:700], end="...\n\n")

print("Metadados da página:", str(docs[0].metadata))
