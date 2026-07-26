import re
import pandas as pd
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import streamlit as st

factory = StemmerFactory()
stemmer = factory.create_stemmer()
stop_words = set(stopwords.words("indonesian"))

def case_folding(text):
    return str(text).lower()

def tokenizing(text):
    text = re.sub(r"[^\w\s]", " ", text)
    return text.split()

def stopword_removal(tokens):
    return [t for t in tokens if t not in stop_words]

def stemming(tokens):
    return [stemmer.stem(t) for t in tokens]

def preprocess_text(text):
    text = case_folding(text)
    tokens = tokenizing(text)
    tokens = stopword_removal(tokens)
    tokens = stemming(tokens)
    return " ".join(tokens)

def show_preprocessing():
    st.markdown("<h3 id='preprocessing'>🧹 Preprocessing</h3>", unsafe_allow_html=True)

    if "dataset" not in st.session_state:
        st.warning("Silakan upload dataset terlebih dahulu.")
        return

    df = st.session_state.dataset.copy()

    if "Judul Media Nasional" not in df.columns:
        st.error("Kolom 'Judul Media Nasional' tidak ditemukan.")
        return

    hasil = pd.DataFrame()
    hasil["Judul Media Nasional"] = df["Judul Media Nasional"].astype(str)
    hasil["Case Folding"] = hasil["Judul Media Nasional"].apply(case_folding)
    hasil["Tokenizing"] = hasil["Case Folding"].apply(tokenizing)
    hasil["Stopword Removal"] = hasil["Tokenizing"].apply(stopword_removal)
    hasil["Stemming"] = hasil["Stopword Removal"].apply(stemming)
    hasil["Final Text"] = hasil["Stemming"].apply(lambda x: " ".join(x))

    st.dataframe(hasil, use_container_width=True)
    st.session_state["preprocessing"] = hasil
