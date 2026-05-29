import streamlit as st
from openai import OpenAI
import time

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="AI Virtual Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS DESIGN
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: #00FFD1;
    font-size: 50px;
}

.stChatInput {
    position: fixed;
    bottom: 20px;
}

.user-msg {
    background-color: #1E293B;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.bot-msg {
    background-color: #111827;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# OPENROUTER CLIENT
# -----------------------------

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.write("### 🤖 Model")
    model_name = st.selectbox(
        "Choose AI Model",
        [
            "openai/gpt-oss-20b:free"
        ]
    )

    st.markdown("---")

    st.write("### ℹ️ About")
    st.info(
        """
        This AI chatbot is built using:

        - Streamlit
        - OpenRouter API
        - OpenAI SDK
        - LLM Models
        """
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# MAIN TITLE
# -----------------------------

st.title("🤖 AI Virtual Assistant")

st.markdown(
    "<center>Your own Generative AI Chatbot</center>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# SESSION STATE
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# DISPLAY OLD CHATS
# -----------------------------

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-msg">
            👨‍💻 <b>You:</b><br>
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="bot-msg">
            🤖 <b>AI:</b><br>
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# USER INPUT
# -----------------------------

prompt = st.chat_input("Type your message here...")

# -----------------------------
# AI RESPONSE
# -----------------------------

if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show typing spinner
    with st.spinner("AI is thinking..."):

        response = client.chat.completions.create(
            model=model_name,
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=500
        )

        answer = response.choices[0].message.content

        time.sleep(1)

    # Store AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()