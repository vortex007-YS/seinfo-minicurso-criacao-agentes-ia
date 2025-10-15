import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

"""Utilize essa classe para o desafio proposto no Minicurso"""

class ChatBot:
    def __init__(self):
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY não encontrada")
        
        self.llm = None # Inicialize o modelo de linguagem aqui, por exemplo: ChatGoogleGenerativeAI(model="...") 
    
    def gerar_resposta(self, mensagens: list[dict[str, str]]) -> str:
        try:
            response = "🚧 Olá, estou em desenvovimento ainda 🏗️" # Implemente a lógica para gerar a resposta utilizando o modelo de linguagem aqui
            # exemplo de uso do llm com classe: self.llm.invoke(mensagens)
            
            if hasattr(response, 'content'):
                return response.content
            else:
                return str(response)
                
        except Exception as e:
            return f"Erro ao gerar resposta: {str(e)}"