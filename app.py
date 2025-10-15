import streamlit as st
from desafio.chatbot import ChatBot

st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main {
        padding-top: 2rem;
        background-color: #f8f9fa;
    }
    
    .stChatMessage[data-testid="user-message"] {
        background: linear-gradient(135deg, #4CAF50, #45a049) !important;
        color: white !important;
        border-radius: 15px 15px 5px 15px !important;
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
        border: none !important;
    }
    
    .stChatMessage[data-testid="assistant-message"] {
        background: linear-gradient(135deg, #2196F3, #1976D2) !important;
        color: white !important;
        border-radius: 15px 15px 15px 5px !important;
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
        border: none !important;
    }
    
    .stChatMessage {
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        margin-bottom: 1rem !important;
    }
    
    .stChatMessage p {
        color: white !important;
        margin: 0 !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
    }
    
    .stChatMessage .stAvatar {
        background-color: rgba(255,255,255,0.2) !important;
        border-radius: 50% !important;
    }
    
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #4CAF50;
        padding: 0.75rem 1rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #2196F3 !important;
        box-shadow: 0 0 10px rgba(33, 150, 243, 0.3) !important;
    }
    
    .title-header {
        text-align: center;
        color: #2E7D32;
        font-size: 3rem;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .chat-input-container {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 1rem 0;
        border-top: 1px solid #e0e0e0;
        margin-top: 2rem;
    }
    
    .stButton > button {
        border-radius: 20px;
        border: none;
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stSpinner {
        color: #2196F3 !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def init_chatbot():
    return ChatBot()

try:
    chatbot = init_chatbot()
except ValueError as e:
    st.error(f"⚠️ {e}")
    st.stop()

# Inicialização do histórico
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Olá! Pergunte qualquer coisa"
    })

st.markdown('<h1 class="title-header">ChatBot</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown("### 📚 Como usar")
    st.markdown("- Faça qualquer pergunta ao modelo!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown("### 💡 Dicas")
    st.markdown("""
    - Seja específico nas suas perguntas
    - Use exemplos quando possível
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🗑️ Limpar Conversa", use_container_width=True):
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()

chat_container = st.container()

user_input = st.chat_input("Digite sua pergunta aqui...", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Pensando... 🤔"):
        try:
            response_content = chatbot.gerar_resposta(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response_content})
        except Exception as e:
            error_msg = f"Desculpe, ocorreu um erro: {str(e)}"
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    st.rerun()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #666; font-size: 0.8rem;">Powered by Streamlit & LangChain 🚀</p>',
    unsafe_allow_html=True
)
