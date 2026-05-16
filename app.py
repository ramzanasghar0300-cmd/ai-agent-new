<<<<<<< HEAD
import streamlit as st
from langchain_groq import ChatGroq

st.title("🤖 LangChain + Groq AI Agent")

api_key = st.secrets["GROQ_API_KEY"]

question = st.text_input("Ask Anything")

if st.button("Ask AI"):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile"
    )

    response = llm.invoke(question)

    st.write(response.content) # AI Agent
=======
import streamlit as st
from langchain_groq import ChatGroq

st.title("🤖 LangChain + Groq AI Agent")

api_key = st.secrets["GROQ_API_KEY"]

question = st.text_input("Ask Anything")

if st.button("Ask AI"):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile"
    )

    response = llm.invoke(question)

    st.write(response.content)
>>>>>>> f9fd07e958b13758b3201213005b16977f339a13
