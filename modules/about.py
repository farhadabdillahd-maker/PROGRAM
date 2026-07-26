import streamlit as st
import os

def show_about():
    st.markdown("<h3 id='about'>👨‍💻 About Aplikasi</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    with col1:
        if os.path.exists("assets/FOTO.png"):
            st.image("assets/FOTO.png", use_container_width=True)
        else:
            st.info("Foto tidak ditemukan.")

    with col2:
        st.markdown("""
### PENERAPAN MACHINE LEARNING MENGGUNAKAN ALGORITMA NAÏVE BAYES
#### UNTUK KLASIFIKASI TINGKAT KEJAHATAN

**Studi Kasus:** Polres Pasaman

Aplikasi ini dikembangkan untuk membantu proses klasifikasi tingkat kejahatan
menggunakan tahapan NLP (Case Folding, Tokenizing, Stopword Removal,
Stemming), pembobotan TF-IDF, dan algoritma Multinomial Naïve Bayes.

---
**Pengembang**

- **Nama:** FARHAD ABDILLAH DARNAZ
- **Jurusan:** Teknik Informatika

**Fitur Aplikasi**
- Upload Dataset
- Preprocessing
- TF-IDF
- Klasifikasi Naïve Bayes
- Prediksi Tingkat Kejahatan
- Laporan Hasil
""")

    st.success("Terima kasih telah menggunakan aplikasi ini.")

