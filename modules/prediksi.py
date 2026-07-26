import streamlit as st
import joblib

def show_prediksi():
    st.markdown("<h3 id='prediksi'>🔍 Prediksi Tingkat Kejahatan</h3>", unsafe_allow_html=True)

    if "model" in st.session_state:
        model = st.session_state["model"]
    else:
        try:
            model = joblib.load("model_naive_bayes.joblib")
        except Exception:
            st.error("Model belum tersedia. Jalankan proses klasifikasi terlebih dahulu.")
            return

    if "tfidf_vectorizer" in st.session_state:
        vectorizer = st.session_state["tfidf_vectorizer"]
    else:
        st.error("TF-IDF Vectorizer belum tersedia.")
        return

    judul = st.text_area(
        "Masukkan Judul Berita",
        placeholder="Contoh: Pelaku pencurian sepeda motor berhasil diamankan polisi"
    )

    if st.button("Prediksi"):
        if not judul.strip():
            st.warning("Masukkan judul berita terlebih dahulu.")
            return

        X = vectorizer.transform([judul])
        hasil = model.predict(X)[0]

        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(X).max() * 100
        else:
            prob = None

        st.success(f"Hasil Prediksi : {hasil}")

        if prob is not None:
            st.metric("Tingkat Keyakinan", f"{prob:.2f}%")

        st.session_state["hasil_prediksi"] = {
            "judul": judul,
            "hasil": hasil,
            "probabilitas": prob,
        }
