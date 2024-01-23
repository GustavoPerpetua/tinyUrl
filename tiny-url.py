import streamlit as st
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

# Web app configuration
st.set_page_config(page_title="tinyUrl", page_icon="😃", layout="centered")
st.title("URL Shortener")

# Input for URL
url = st.text_input("Enter URL")

# Button to generate short URL
if st.button("Generate new URL"):
    shortened_url = shorten_url(url)
    st.write("Shortened URL:", shortened_url)