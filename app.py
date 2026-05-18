import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    st.write(answer)