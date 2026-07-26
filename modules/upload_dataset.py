import streamlit as st
import pandas as pd

def show_upload_dataset():
    """Menu Upload Dataset"""

    if "uploaded_dataset" not in st.session_state:
        st.session_state.uploaded_dataset = None

    st.markdown("### 📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload Dataset CSV",
        type=["csv"],
        key="dashboard_upload"
    )

    if uploaded_file is not None:
        try:
            uploaded_file.seek(0)
        except Exception:
            pass

        st.session_state.uploaded_dataset = uploaded_file

        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file)
            uploaded_file.seek(0)

            st.session_state["df"] = df

            st.success("Dataset berhasil diupload.")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Gagal membaca dataset: {e}")

    if st.session_state.uploaded_dataset is not None:
        if st.button("🔄 Repeat", use_container_width=True):
            st.session_state.uploaded_dataset = None

            if "dashboard_upload" in st.session_state:
                del st.session_state["dashboard_upload"]

            if "df" in st.session_state:
                del st.session_state["df"]

            st.rerun()
