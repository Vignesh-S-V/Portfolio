import streamlit as st
import streamlit.components.v1 as components

# Page Title
st.set_page_config(page_title="My Website", layout="wide")

# Read your HTML file
with open("index.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Render HTML in Streamlit
components.html(html_content, height=1000, scrolling=True)