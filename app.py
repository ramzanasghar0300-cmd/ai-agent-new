import streamlit as st
from groq import Groq

st.title("🤖 AI Agent")

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

question = st.text_input("Ask Anything")

if st.button("Ask AI"):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    st.write(chat_completion.choices[0].message.content)