import streamlit as st

# Title of the app
st.title("Questionnaire")

# Function to create a question with Yes/No/Unknown options
def create_question(question_text, key):
    st.radio(question_text, options=["Yes", "No", "Unknown"], key=key)

# List of 20 questions
questions = [
    "Question 1: Is the sky blue?",
    "Question 2: Is water wet?",
    "Question 3: Is fire hot?",
    "Question 4: Do birds fly?",
    "Question 5: Do fish swim?",
    "Question 6: Is the earth round?",
    "Question 7: Is the sun a star?",
    "Question 8: Is snow cold?",
    "Question 9: Is the moon made of cheese?",
    "Question 10: Can humans breathe underwater without equipment?",
    "Question 11: Is coffee a beverage?",
    "Question 12: Do trees produce oxygen?",
    "Question 13: Is ice cream a dessert?",
    "Question 14: Is chocolate sweet?",
    "Question 15: Are apples fruits?",
    "Question 16: Is milk white?",
    "Question 17: Do cars run on gasoline?",
    "Question 18: Is gold a metal?",
    "Question 19: Can planes fly?",
    "Question 20: Is sugar sweet?"
]

# Creating the questions
for i, question in enumerate(questions):
    create_question(question, key=f"question_{i+1}")

# Submit button
if st.button("Submit"):
    responses = {f"question_{i+1}": st.session_state[f"question_{i+1}"] for i in range(len(questions))}
    st.write("Responses:", responses)
