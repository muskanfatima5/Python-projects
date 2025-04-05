import streamlit as st
import random
import time


st.title("📜 Quiz Application")

questions = [
    {
        "question" : "What is the capital of Pakistan?",
        "options" : ["Karachi", "Islamabad", "Lahore", "Peshawar"],
        "answer" : "Islamabad"
    },
    {
        "question" : "Who is the Founder of Pakistan?",
        "options" : ["Allama Iqbal", "Muhammad Ali Jinnah", "Liaquat Ali Khan", "Fatima Jinnah"],
        "answer" : "Muhammad Ali Jinnah"
    },
    {
        "question" : "What is the national Languagre of Pakistan?",
        "options" : ["Punjabi", "English", "Urdu", "Sindhi"],
        "answer" : "Urdu"
    },
    {
        "question" : "What is the currency of Pakistan?",
        "options" : ["Yen", "Dollar", "Pound", "Rupee"],
        "answer" : "Rupee"
    },
    {
        "question" : "Which city is known as the city of lights in Pakistan?",
        "options" : ["Islamabad", "Lahore", "IslamabadKarachi", "Peshawar"],
        "answer" : "Karachi"
    }
]


if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Select an option", question["options"], key="answer")


if st.button("Submit Answer"):
    if selected_option == question["answer"]:
      st.success("✔ Correct Answer!")
      st.balloons()
    else:
      st.error("❌ Wrong Answer! The correct answer is: "+ question["answer"])


    time.sleep(3)
    st.session_state.current_question = random.choice(questions)

    st.rerun()
