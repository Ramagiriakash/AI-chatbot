import os
import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

st.title("AI Chatbot")

question = st.text_input("Ask me anything:")

if st.button("Send"):
    if question:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content
        st.write("Bot:", answer)
