# Para realizar esse exemplo, você precisa:
# 1. baixar o Ollama: https://ollama.com/download
# 2. Instale o modelo: ollama pull deepseek-r1:7b
# 3. Instale as dependências:
# pip install langchain-ollama==0.3.10
#
# Mais informações em: https://python.langchain.com/api_reference/ollama/llms/langchain_ollama.llms.OllamaLLM.html#ollamallm

try:
    from langchain_ollama import OllamaLLM
except ImportError:
    print("⚠️ Por favor, instale a biblioteca langchain-ollama: pip install langchain-ollama==0.3.10")
    exit(1)


llm = OllamaLLM(
    model="deepseek-r1:1.5b",
    temperature=0.3,
    num_predict=256,
    think=True
)

pergunta = "Quem foi Albert Einstein?"

print("Resposta do modelo usando invoke (pode demorar um pouco):")
resposta = llm.invoke(pergunta)
print(resposta)

print("-"*40)

import asyncio
async def stream_response():
    async for chunk in llm.astream(pergunta):
        print(chunk, end="")

print("Resposta do modelo usando streaming e chamada assíncrona:")
asyncio.run(stream_response())

print()  # Para adicionar uma nova linha após o streaming