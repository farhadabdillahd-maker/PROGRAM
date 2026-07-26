import streamlit as st

def show_home():
    st.markdown("""
    <div style='padding:60px;border-radius:28px;background:rgba(8,27,70,.55);
    backdrop-filter:blur(8px);color:#fff;
    box-shadow:0 20px 45px rgba(0,0,0,.28);
    border:1px solid rgba(255,255,255,.12)'>
        <div style='font-size:15px;letter-spacing:2px;color:#bfdbfe'>
        POLRES PASAMAN • MACHINE LEARNING • NAÏVE BAYES
        </div>
        <h1 style='font-size:42px;font-weight:900;line-height:1.35;'>
        PENERAPAN MACHINE LEARNING MENGGUNAKAN ALGORITMA NAÏVE BAYES
        <br>UNTUK KLASIFIKASI TINGKAT KEJAHATAN
        </h1>
        <div style='font-size:19px;margin-top:18px;font-weight:500'>
        Studi Kasus Data Kriminal Polres Pasaman
        </div>
    </div>
    """, unsafe_allow_html=True)

    a,b,c,d = st.columns(4)
    a.metric("📂 Dataset","CSV")
    b.metric("🤖 Model","Naïve Bayes")
    c.metric("🧹 NLP","TF-IDF + Stemming")
    d.metric("📄 Output","Prediksi & Surat")

    st.markdown("### 🔄 Alur Sistem")
    st.markdown("""
    Upload Dataset ➜ Preprocessing ➜ TF-IDF ➜ Naïve Bayes ➜ Evaluasi ➜ Prediksi ➜ Riwayat
    """)

