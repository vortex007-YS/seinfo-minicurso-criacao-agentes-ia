import os
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)

# Exemplos tirados da documentação do LangChain:
# python.langchain.com/docs/how_to/tool_results_pass_to_model/
@tool
def add(a: int, b: int) -> int:

    return a + b

@tool
def multiply(a: int, b: int) -> int:
    
    return a * b

tools = [add, multiply]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm_with_tools = llm.bind_tools(tools)

print("Digite sua pergunta ou 'sair' para encerrar: ")
messages = []

while (pergunta := input("user: ")) != "sair":
    messages.append(HumanMessage(content=pergunta))
    resposta = llm_with_tools.invoke(messages)

    if resposta.tool_calls:
        messages.append(resposta)

        for tool_call in resposta.tool_calls:
            print(">> LLM solicitou uso da ferramenta:", tool_call['name'])
            selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
            tool_msg = selected_tool.invoke(tool_call)

            print(">> Resposta da ferramenta:", tool_msg.content)
            messages.append(tool_msg)

        resposta = llm_with_tools.invoke(messages)
        messages.append(resposta)

    print("\n llm:", resposta.content, "\n")