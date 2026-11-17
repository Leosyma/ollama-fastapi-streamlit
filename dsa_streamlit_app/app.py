# Lab 6 - Deploy de API Para Aplicação de IA com Ollama, Streamlit e Docker Compose

# Imports
import os
import streamlit as st
import requests

# Configuração da página do Streamlit
st.set_page_config(page_title = "Local language model with Ollama", page_icon = ":100:", layout = "centered")

# Título principal
st.title("🧪 Lab 6 - Deploy de API Para Aplicação de IA com Ollama, Streamlit e Docker Compose")

# Barra lateral com instruções
st.sidebar.header("🚀 Instruções")
st.sidebar.markdown("""
1. **Digite** uma pergunta.
2. O chatbot irá responder usando o modelo **Llama3** através da API do Ollama.
3. IA comete erros. SEMPRE verifique as respostas.

---

**💡 Exemplo de perguntas:**
- _"O que é investimento no Tesouro Direto?"_
- _"Qual o sentido da vida?"_
- _"Quais são as vantagens do modelo Llama3?"_
""")

# Inicializa mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua mensagem aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Envia para API com spinner
    with st.spinner("A IA está processando sua solicitação. Seja paciente e aguarde..."):
        response = requests.post(
            f"{os.getenv('API_URL')}/chat",
            json={"message": prompt}
        )

    # Recebe resposta do chatbot
    assistant_response = response.json()["response"]
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)





        