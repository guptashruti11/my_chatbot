import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Shruti's AI Chatbot", page_icon="🤖")
st.title("💬 Shruti's Gen AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You: ", "")

if st.button("Send") and user_input.strip() != "":
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.chat_history
    )

    bot_reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Bot:** {chat['content']}")
