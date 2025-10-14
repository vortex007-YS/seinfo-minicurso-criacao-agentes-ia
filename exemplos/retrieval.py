import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI


if not os.getenv("GOOGLE_API_KEY"):
    print("Variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1. Configura embeddings Google
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

DB_NAME = "faiss/minecraft_redstone"

# Verificar se o banco de dados já existe
if os.path.exists(f"{DB_NAME}/index.faiss"):
    # Carregar vector database existente
    db = FAISS.load_local(DB_NAME, embeddings, allow_dangerous_deserialization=True)
    print("Vector database carregado com sucesso!")
else:
    # Criar nova vector database
    print("Criando nova vector database...")
    
    # 2. Carregar documentos
    loader = TextLoader("dados.txt")
    documents = loader.load()
    
    # 3. Dividir em chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    
    # 4. Criar vector database
    db = FAISS.from_documents(texts, embeddings)
    
    # 5. Salvar localmente
    db.save_local(DB_NAME)
    print("Vector database criado e salvo com sucesso!")

# 6. Fazer busca por similaridade
pergunta = "Como liga um circuito de redstone?"
docs_retornados = db.similarity_search(pergunta, k=3)

print(f"Pergunta: {pergunta}")
print(f"\nDocumentos mais relevantes encontrados ({len(docs_retornados)} resultados):\n")

for i, doc in enumerate(docs_retornados):
    print(f"--- Documento {i+1} ---")
    print(doc.page_content)
    print("----\n")

# 7. (Opcional) Usar Gemini para gerar resposta baseada nos documentos
if docs_retornados:
    
    contexto = "\n".join([doc.page_content for doc in docs_retornados])
    
    prompt = f"""
    Com base nas seguintes informações sobre Minecraft Redstone:
    
    {contexto}
    
    Responda de forma clara e direta: {pergunta}
    """
    
    try:
        resposta = llm.invoke(prompt)
        print("Resposta do Gemini baseada nos documentos:")
        print(resposta.text)
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")