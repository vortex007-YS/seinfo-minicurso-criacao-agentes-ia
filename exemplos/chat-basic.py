import dotenv, os
from langchain_google_genai import ChatGoogleGenerativeAI

dotenv.load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    exit(1)


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
print("Pressione Enter para fazer uma pergunta ou 'q' para sair: ")

while (pergunta := input("user: ")) != "q":
    messages = [{"role": "user", "content": pergunta}]
    resposta = llm.invoke(messages)

    print("\n llm:", resposta.content, "\n")