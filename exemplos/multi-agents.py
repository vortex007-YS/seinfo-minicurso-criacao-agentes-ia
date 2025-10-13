import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor, Agent, Tool, create_react_agent


load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)


llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash') 

prompt1 = PromptTemplate.from_template("Você é um poeta. Escreva um poema em francês sobre {input}.")
sub_agent_1 = prompt1 | llm

prompt2 = PromptTemplate.from_template("Você é um crítico de filmes. Analise o filme {input}. Sua crítica deve incluir uma breve sinopse e uma nota de 1 a 5.")
sub_agent_2 = prompt2 | llm

tools = [
    Tool(
        name="Poeta",
        func=lambda question: sub_agent_1.invoke({"input": question}).content,
        description="Escreve poemas sobre qualquer assunto"
    ),
    Tool(
        name="Crítico de Filmes", 
        func=lambda question: sub_agent_2.invoke({"input": question}).content,
        description="Analisa e critica filmes"
    )
]


prompt_template = PromptTemplate.from_template("""Você é um assistente que pode atuar como poeta ou crítico de filmes. 
Responda as seguintes perguntas da melhor maneira possível. Você tem acesso às seguintes ferramentas:

{tools}

Use o seguinte formato:

Question: a pergunta de entrada que você deve responder
Thought: você deve sempre pensar sobre o que fazer
Action: a ação a ser tomada, deve ser uma de [{tool_names}]
Action Input: a entrada para a ação
Observation: o resultado da ação
... (este ciclo Thought/Action/Action Input/Observation pode repetir N vezes)
Thought: Agora sei a resposta final
Final Answer: a resposta final para a pergunta original

Comece!

Question: {input}
Thought:{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt=prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True, max_iterations=3)

pergunta = input("Faça uma pergunta sobre filmes ou peça um poema: ")
saida = agent_executor.invoke({"input": pergunta})
print("Saída:\n",saida['output'])