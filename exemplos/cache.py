import os
from dotenv import load_dotenv
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache


load_dotenv()


if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")



set_llm_cache(InMemoryCache())

inicio=time.time()
resposta=llm.invoke("Tell me a joke")
fim=time.time()

inicio2=time.time()
resposta1=llm.invoke("Tell me a joke")
fim2=time.time()


print(resposta)
print(resposta1)
print(f"Tempo de execução: {fim - inicio:.2f} segundos")
print(f"Tempo de execução: {fim2 - inicio2:.2f} segundos")