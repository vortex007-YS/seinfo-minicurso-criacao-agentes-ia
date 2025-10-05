import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
print("Digite sua pergunta ou 'sair' para encerrar: ")

messages = []

while (pergunta := input("user: ")) != "sair":
    messages.append({"role": "user", "content": pergunta})
    resposta = llm.invoke(messages)
    messages.append({"role": "assistant", "content": resposta.content})
    print("\n llm:", resposta.content, "\n")