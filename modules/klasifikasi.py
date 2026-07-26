import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

def show_klasifikasi():
    st.markdown("<h3 id='klasifikasi'>🤖 Klasifikasi Naïve Bayes</h3>", unsafe_allow_html=True)

    if "tfidf_matrix" not in st.session_state:
        st.warning("Silakan lakukan proses TF-IDF terlebih dahulu.")
        return

    df = st.session_state["preprocessing"]

    if "Label" not in df.columns:
        st.error("Kolom 'Label' tidak ditemukan.")
        return

    X = st.session_state["tfidf_matrix"]
    y = df["Label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred, average="weighted", zero_division=0)
    rec = recall_score(y_test, y_pred, average="weighted", zero_division=0)
    f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Accuracy", f"{acc:.2%}")
    c2.metric("Precision", f"{pre:.2%}")
    c3.metric("Recall", f"{rec:.2%}")
    c4.metric("F1-Score", f"{f1:.2%}")

    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(5,4))
    ax.imshow(cm)
    ax.set_xlabel("Prediksi")
    ax.set_ylabel("Aktual")
    ax.set_xticks(range(len(model.classes_)))
    ax.set_yticks(range(len(model.classes_)))
    ax.set_xticklabels(model.classes_)
    ax.set_yticklabels(model.classes_)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, str(cm[i,j]), ha="center", va="center")
    st.pyplot(fig)

    st.subheader("Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(pd.DataFrame(report).transpose(), use_container_width=True)

    joblib.dump(model, "model_naive_bayes.joblib")

    st.session_state["model"] = model
    st.session_state["X_test"] = X_test
    st.session_state["y_test"] = y_test
