from openai import OpenAI
import streamlit as st

# Read the API key and setup an OpenAI client
with open("openai_key/.openai_key.txt") as f:
    openai_api_key = f.read().strip()

# Set the title and color of the title
st.title("GenAI App - AI Code Reviewer")
st.markdown("<h2 style='color:blue;'>Python Code Reviewer and Bug Fixer</h2>", unsafe_allow_html=True)

# Initialize OpenAI client with the API key
client = OpenAI(api_key=openai_api_key)

# Take user's input
prompt = st.text_area("Enter your Python code", height=200)

# If button is clicked, generate responses
if st.button("Get Review"):
    st.markdown("<h3 style='color:black;'>Review:</h3>", unsafe_allow_html=True)

    # Original Code
    st.markdown("<h4 style='color:green;'>Original Code:</h4>", unsafe_allow_html=True)
    st.code(prompt, language='python')

    # Request code review from OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI Assistant. Given a Python code snippet, you will review it for potential bugs and suggest fixes."},
            {"role": "user", "content": prompt}
        ]
    )

    # Display corrected code
    corrected_code = response.choices[0].message.content
    st.markdown("<h4 style='color:blue;'>Corrected Code and Review:</h4>", unsafe_allow_html=True)
    st.code(corrected_code, language='python')
