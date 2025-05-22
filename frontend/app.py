import streamlit as st
import requests

st.title("Multi-Agent QA Bot")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Ask me anything about credit report, bank statement, EID of a customer:")

if question:
    st.session_state.chat.append(("user", question))
    with st.spinner("Thinking..."):
        res = requests.post("http://localhost:8080/ask", json={"question": question})
        print(res.status_code)
        print(res.text)
        answer = res.json().get("answer", "No answer")
        st.session_state.chat.append(("bot", answer))

for sender, message in st.session_state.chat:
    if sender == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
