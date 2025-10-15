# **Introdução à criação de agentes de IA com bancos de vetores**

📋 Visão Geral do Curso

O minicurso tem como objetivo instruir os participantes na construção de um agente de IA capaz de responder a perguntas sobre documentos específicos.

Para tal, será utilizada uma Large Language Model (LLM) para gerar respostas inteligentes, integrada a um banco de dados vetorial (FAISS), responsável por fornecer o contexto preciso a partir dos documentos. O framework LangChain será empregado para orquestrar a aplicação de forma eficiente.

É pré-requisito para o minicurso possuir noções básicas da linguagem de programação Python

## 🎯 Objetivos do Curso

- Criar um chatbot usando framework langchain e API gratuita do Gemini
- Introduzir a criação de agentes de IA
- Fundamentos de Retrieval Augmentation Generation (RAG) e bancos de dados de vetores

## 👥 Público-Alvo

- Interessados em IA Generativa
- Estudantes de Sistemas de Informação que participaram do Minicurso na SEINFO 2025

## 🚀 Preparação do Ambiente

### 1. Clonando o repositório

```bash
git clone https://github.com/JosianaSilva/seinfo-minicurso-criacao-agentes-ia.git
cd seinfo-minicurso-criacao-agentes-ia
```

### 2. Criando e ativando o ambiente virtual

**No Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**No Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**No Git Bash:**
```bash
python -m venv venv
source venv/Scripts/activate
```

**No Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Configurando variáveis de ambiente

1. Copie o arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env` e configure sua chave da API do Google:
   ```bash
   GOOGLE_API_KEY=sua_chave_aqui
   ```

   > 💡 **Dica:** Para obter sua chave da API do Google Gemini, acesse [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. Instalando as dependências

```bash
pip install -r requirements.txt
```

### 5. Executando o exemplo básico

Para testar se tudo está funcionando corretamente, execute o chat básico:

```bash
python exemplos/chat-basic.py
```

Você também pode explorar outros exemplos disponíveis na pasta `exemplos/`:
- `vector-store-basic.py` - Exemplo básico de banco de vetores
- `pdf-document-loader.py` - Carregamento de documentos PDF
- `tool-basic.py` - Exemplo de ferramenta básica
- E muitos outros!

## 🏆 Desafio Final

Após explorar os exemplos, implemente um chatbot que combine pelo menos uma **tool** (ferramenta) e um **vector store** (banco de vetores). O objetivo é criar um agente inteligente que possa:

- Responder perguntas usando conhecimento armazenado em um banco de vetores
- Executar ações através de ferramentas personalizadas
- Integrar ambas as funcionalidades de forma harmoniosa

### 📋 Requisitos do Desafio
1. **Modelo**: Utilizar o modelo Gemini para geração de respostas  
2. **Vector Store**: Implementar um banco de vetores usando FAISS para armazenar e recuperar informações
3. **Tool**: Criar pelo menos uma ferramenta customizada que o agente possa utilizar
5. **Interface** (Opcional): Utilizar a interface já desenvolvida com Streamlit para conectar o chatbot.

### 🚀 Executando o Desafio

O desafio deve ser executável em uma das de duas formas:

#### Opção 1: Interface Web com Streamlit (Recomendado)
```bash
streamlit run app.py
```

#### Opção 2: Chatbot via Terminal
```bash
python desafio/chatbot.py
```

### 💡 Dicas para o Desenvolvimento

- Explore os exemplos na pasta `exemplos/` para entender como implementar tools e vector stores
- Use o arquivo `app.py` como base para a interface Streamlit
- Implemente sua lógica principal no arquivo `desafio/chatbot.py`
- Teste diferentes combinações de ferramentas e tipos de documentos

---

## 👥 Autores

<table border="0">
  <tr>
    <td align="center">
      <a href="https://github.com/gabalencar">
        <img src="https://github.com/gabalencar.png" width="100px;" alt="Gabriel"/>
        <br />
        <sub><b>Gabriel Alencar Gomes</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/JosianaSilva">
        <img src="https://github.com/JosianaSilva.png" width="100px;" alt="Josiana"/>
        <br />
        <sub><b>Josiana Silva</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/rosemelry">
        <img src="https://github.com/rosemelry.png" width="100px;" alt="Rosemelry"/>
        <br />
        <sub><b>Rosemelry Mendes</b></sub>
      </a>
    </td>
  </tr>
</table>