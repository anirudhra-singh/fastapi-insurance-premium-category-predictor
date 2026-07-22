import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

st.title("Insurance Premium Category Predictor")
st.markdown("## Enter your details below:")

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)

smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")

occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job',
     'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):

    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:

        with st.spinner("Predicting..."):
            response = requests.post(API_URL, json=input_data, timeout=5,)

        if response.status_code == 200:

            result = response.json()

            category = result["predicted_category"]
            confidence = result["confidence"]
            probabilities = result["class_probabilities"]

            st.markdown("---")
            st.subheader("Prediction Result")

            # Category Card
            if category.lower() == "low":
                st.success(f" Predicted Category: **{category}**")
            elif category.lower() == "medium":
                st.warning(f"Predicted Category: **{category}**")
            else:
                st.error(f"Predicted Category: **{category}**")

            # Metrics
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="Confidence",
                    value=f"{confidence * 100:.1f}%"
                )

            with col2:
                st.metric(
                    label="Category",
                    value=category
                )

            st.markdown("### Class Probabilities")

            for cls, prob in probabilities.items():
                st.write(f"**{cls}**")
                st.progress(float(prob))
                st.caption(f"{prob * 100:.1f}%")

            st.markdown("### Prediction Summary")

            st.info(
                f"""
**Category:** {category}

**Confidence:** {confidence * 100:.1f}%

 Prediction generated successfully.
"""
            )

        else:
            st.error(f"❌ API Error: {response.status_code}")
            st.write(response.json())

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to FastAPI server. Is it running?")

    except Exception as e:
        st.error(f"Unexpected Error: {e}")