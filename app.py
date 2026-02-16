import streamlit as st
from classifier import classify_text
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Misinformation Detection", layout="centered")

st.title("🔍 LLM-Based Misinformation Detection System")
st.markdown("This system uses a HuggingFace LLM (DistilBART-MNLI) to classify news as Real or Fake.")

text = st.text_area("Enter News Text")

if st.button("Analyze"):
    if text:
        with st.spinner("Analyzing..."):
            label, confidence, explanation = classify_text(text)

        st.subheader("📊 Prediction Results")

        if label == "Real News":
            st.success(f"Label: {label}")
        else:
            st.error(f"Label: {label}")

        st.progress(confidence)
        st.write(f"Confidence: {confidence}")
        st.write(f"Explanation: {explanation}")

        # Logging
        os.makedirs("logs", exist_ok=True)
        log_file = "logs/predictions.csv"

        new_entry = pd.DataFrame([{
            "timestamp": datetime.now(),
            "text": text,
            "prediction": label,
            "confidence": confidence
        }])

        if os.path.exists(log_file):
            old = pd.read_csv(log_file)
            updated = pd.concat([old, new_entry])
        else:
            updated = new_entry

        updated.to_csv(log_file, index=False)