import streamlit as st

from modules.home import show_home
from modules.upload_dataset import show_upload_dataset
from modules.preprocessing import show_preprocessing
from modules.tfidf import show_tfidf
from modules.klasifikasi import show_klasifikasi
from modules.prediksi import show_prediksi
from modules.about import show_about

st.set_page_config(
    page_title="Klasifikasi Tingkat Kejahatan",
    page_icon="🛡️",
    layout="wide"
)

menu = st.sidebar.radio(
    "Menu",
    [
        "Home",
        "Upload Dataset",
        "Preprocessing",
        "TF-IDF",
        "Klasifikasi",
        "Prediksi",
        "About"
    ]
)

if menu == "Home":
    show_home()
elif menu == "Upload Dataset":
    show_upload_dataset()
elif menu == "Preprocessing":
    show_preprocessing()
elif menu == "TF-IDF":
    show_tfidf()
elif menu == "Klasifikasi":
    show_klasifikasi()
elif menu == "Prediksi":
    show_prediksi()
elif menu == "About":
    show_about()
