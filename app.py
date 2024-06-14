import streamlit as st

##################################### SIDE BAR #######################################
def sidebar():
    st.sidebar.title("User Authentication")
    
    email = st.sidebar.text_input("Email")
    list_departments = ["DA", "TDAA"]
    department = st.sidebar.selectbox("Select Department", list_departments)
    password = st.sidebar.text_input("Password", type="password", key="password")

    if st.sidebar.button("Login"):
        if authenticate_user(email, password):
            st.session_state["authenticated"] = True
            st.session_state["email"] = email
            st.session_state["department"] = department
            st.sidebar.success("Authentication successful")
            st.experimental_set_query_params(page="home")
            st.experimental_rerun()
        else:
            st.sidebar.error("Invalid email or password")

def authenticate_user(email, password):
    # This is a placeholder function for user authentication.
    # Replace it with your actual authentication logic.
    return email == "user@example.com" and password == "password"

if __name__ == "__main__":
    st.set_page_config(page_title="Translation Service", page_icon="📖", layout="wide")
    st.write(addfitz)
    sidebar()
