import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate


load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    print("variável de ambiente GOOGLE_API_KEY não encontrada.")
    exit(1)


llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash') 


prompt_template = PromptTemplate.from_template("Descreva as tendências tecnologicas  em {ano}")
runnable_sequence = prompt_template | llm
saida = runnable_sequence.invoke({"ano":"2025"})

print("Saida:\n",saida)