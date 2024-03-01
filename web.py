import streamlit as st

# Set page title
st.title("Simple Web Page with Streamlit")

# Add a big label and center it
st.header("Enter Your Text Input")

# Add an input field
user_input = st.text_input("Type here:")

# Add a submit button and center it
if st.button("Submit", key="submit_button"):
    pass  # No need to display the entered text
