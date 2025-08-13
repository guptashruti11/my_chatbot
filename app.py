import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("💬 Groq Chatbot")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(response.choices[0].message.content)
