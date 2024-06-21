import streamlit as st

# Title of the app
st.title("Market Edge: Opportunity Scorecard")

# Input fields for project profile
st.header("Project Profile")

company = st.text_input("Company")
solution_service = st.text_input("Solution/Service")
revenue = st.number_input("Revenue", min_value=0.0, format="%f")
close_date = st.date_input("Close Date")
pipeline_stage = st.selectbox("Pipeline Stage", ["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5"])
your_name = st.text_input("Your Name")

# Section for 20 questions
st.header("Definition Rating")

# Function to create a question with Yes/No/Unknown options
def create_question(question_text, key):
    st.radio(question_text, options=["Yes", "No", "Unknown"], key=key)

# List of 20 questions
questions = [
    "Question 1: Does the opportunity align with the company's strategic goals?",
    "Question 2: Is there a clear understanding of the client's needs?",
    "Question 3: Is the budget allocated for this project?",
    "Question 4: Is the timeline for the project realistic?",
    "Question 5: Are the key stakeholders identified?",
    "Question 6: Has the decision-making process been mapped out?",
    "Question 7: Is there a competitive advantage in this opportunity?",
    "Question 8: Are there potential risks identified?",
    "Question 9: Is there a defined project scope?",
    "Question 10: Are the project deliverables clearly defined?",
    "Question 11: Is there a resource plan in place?",
    "Question 12: Are the KPIs for the project defined?",
    "Question 13: Is there a communication plan established?",
    "Question 14: Are there any legal or compliance issues?",
    "Question 15: Is there a contingency plan?",
    "Question 16: Is there a post-implementation support plan?",
    "Question 17: Are there success criteria defined?",
    "Question 18: Is there a customer feedback mechanism?",
    "Question 19: Is there a plan for stakeholder engagement?",
    "Question 20: Is there a quality assurance plan?"
]

# Creating the questions
for i, question in enumerate(questions):
    create_question(question, key=f"question_{i+1}")

# Submit button
if st.button("Submit"):
    responses = {f"question_{i+1}": st.session_state[f"question_{i+1}"] for i in range(len(questions))}
    profile = {
        "Company": company,
        "Solution/Service": solution_service,
        "Revenue": revenue,
        "Close Date": close_date,
        "Pipeline Stage": pipeline_stage,
        "Your Name": your_name
    }
    st.write("Project Profile:", profile)
    st.write("Responses:", responses)