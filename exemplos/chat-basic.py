import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
print("Pressione Enter para fazer uma pergunta ou 'q' para sair: ")

while (pergunta := input("user: ")) != "q":
    messages = [{"role": "user", "content": pergunta}]
    resposta = llm.invoke(messages)

    print("\n llm:", resposta.content, "\n")