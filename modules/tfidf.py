import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def show_tfidf():
    st.markdown("<h3 id='tf-idf'>🔤 TF-IDF</h3>", unsafe_allow_html=True)

    if "preprocessing" not in st.session_state:
        st.warning("Silakan lakukan preprocessing terlebih dahulu.")
        return

    df = st.session_state["preprocessing"].copy()

    if "Final Text" not in df.columns:
        st.error("Kolom 'Final Text' tidak ditemukan.")
        return

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["Final Text"])

    tfidf_df = pd.DataFrame(
        tfidf_matrix.toarray(),
        columns=vectorizer.get_feature_names_out()
    )

    st.subheader("Hasil TF-IDF")
    st.dataframe(tfidf_df, use_container_width=True)

    st.subheader("Kosakata (Vocabulary)")
    st.write(vectorizer.get_feature_names_out())

    st.metric("Jumlah Kata Unik", len(vectorizer.get_feature_names_out()))

    st.session_state["tfidf_vectorizer"] = vectorizer
    st.session_state["tfidf_matrix"] = tfidf_matrix
    st.session_state["tfidf_dataframe"] = tfidf_df
