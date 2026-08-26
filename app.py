import streamlit as st

st.set_page_config(page_title="Vigneshwaran S — Portfolio", layout="wide")

st.markdown("""
<meta http-equiv="refresh" content="0; url=./static/index.html">
<style>
  #MainMenu, header, footer {visibility: hidden;}
</style>
<div style="display:flex;align-items:center;justify-content:center;height:80vh;font-family:sans-serif;">
  <a href="./static/index.html" style="padding:14px 28px;background:#00c8a8;color:#080c18;
     border-radius:4px;text-decoration:none;font-weight:600;letter-spacing:1px;">
     Opening Portfolio — Click here if not redirected →
  </a>
</div>
""", unsafe_allow_html=True)
