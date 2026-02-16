import streamlit as st
import requests

st.set_page_config(page_title="AI Fake News Detector", page_icon="📰")

st.title("📰 AI Fake News Detection System")
st.write("Enter a news headline or article below to classify it.")

user_input = st.text_area("Enter News Text Here:")

if st.button("Analyze News"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing with LLaMA3..."):

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": user_input}
            )

            if response.status_code == 200:
                result = response.json()

                prediction = result["prediction"]
                response_time = result["response_time_seconds"]

                if "Real" in prediction:
                    st.success(f"🟢 Prediction: {prediction}")
                else:
                    st.error(f"🔴 Prediction: {prediction}")

                st.info(f"⏱ Response Time: {response_time} seconds")

            else:
                st.error("Error connecting to backend.")
                