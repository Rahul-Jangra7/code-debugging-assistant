# main.py

import streamlit as st
from debugger import run_syntax_check

# ---------- Page Setup ----------
st.set_page_config(page_title="Code Debugging Assistant", layout="centered")
st.title("Code Debugging Assistant")
st.markdown("Debug your code for syntax errors — fast, clean, and easy.")

# ---------- Language Selection ----------
language = st.selectbox("Choose Language", ["Python", "C++", "Java"])

# ---------- Code Input Area ----------
code_input = st.text_area(
    label="Paste your code here",
    placeholder="Write or paste your code here...",
    height=300
)

# ---------- Check Button ----------
if st.button("Run Syntax Check"):
    if not code_input.strip():
        st.warning("Please enter some code to check.")
    else:
        with st.spinner("Checking for syntax errors..."):
            result = run_syntax_check(code_input, language)
        st.text_area("Result", result, height=200)
