import streamlit as st
from langchain_groq import ChatGroq

st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Assistant")
st.write("Ask me anything!")

api_key = "YOUR_GROQ_KEY"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your question...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile"
    )

    response = llm.invoke(prompt)

    ai_response = response.content

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )

    with st.chat_message("assistant"):
        st.markdown(ai_response)