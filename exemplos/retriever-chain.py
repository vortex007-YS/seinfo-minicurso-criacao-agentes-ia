from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os


llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash') 
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

prompt = ChatPromptTemplate.from_template(
    """Answer the question based only on the context provided.

    Context: {context}

    Question: {question}"""
)

DB_NAME = "faiss/minecraft_redstone"
if not os.path.exists(f"{DB_NAME}/index.faiss"):
    exit("Base de dados FAISS não encontrada. Rode o script para criar a base primeiro.")

db = FAISS.load_local(DB_NAME, embeddings, allow_dangerous_deserialization=True)
print("Carregado com sucesso")

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})


pergunta = "Como liga um circuito de redstone?"
docs_recuperados = retriever.get_relevant_documents(pergunta)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

print("Resultados: \n" + format_docs(docs_recuperados))

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

response = chain.invoke(pergunta)
print("\nResposta do modelo: ")
print(response)