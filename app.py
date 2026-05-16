import streamlit as st
from langchain_groq import ChatGroq

st.title("🤖 LangChain + Groq AI Agent")

api_key = st.secrets["GROQ_API_KEY"]

question = st.text_input("Ask Anything")

if st.button("Ask AI"):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-8b-8192"
    )

    response = llm.invoke(question)

    st.write(response.content)