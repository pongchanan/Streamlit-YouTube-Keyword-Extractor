import streamlit as st
import lxml
from bs4 import BeautifulSoup
import requests

st.markdown("<h1 style='text-align: center'>Youtube Keyboard Extractor</h1>", unsafe_allow_html=True)
st.markdown("---")

url = st.text_input("youtube url here")

if url:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'lxml')
    meta_tag = soup.select("meta[name='keywords']")
    keyword = meta_tag[0]["content"]
    
    st.title("Tags")
    st.markdown(f"<h5>{keyword}</h5>", unsafe_allow_html=True)