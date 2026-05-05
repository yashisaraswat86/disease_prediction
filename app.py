import streamlit as st
import joblib
import numpy as np
import pandas as pd


if "show_result" not in st.session_state:
    st.session_state.show_result = False

if "result_html" not in st.session_state:
    st.session_state.result_html = ""


st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)


model = joblib.load("rf_disease_model.pkl")
encoder = joblib.load("disease_label_encoder.pkl")
symptom_columns = joblib.load("symptom_columns.pkl")


st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

* { font-family: 'Poppins', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.block-container {
    max-width: 700px;
    padding-top: 60px;
}

[data-testid="stVerticalBlock"] {
    background-color: #1c1c1c;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.5);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 600;
    color: #00f5ff;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: #d0d0d0;
    opacity: 0.8;
    margin-bottom: 45px;
}

label {
    opacity: 0.75;
    font-size: 14px;
}

.stButton > button {
    width: 100%;
    background-color: #00f5ff;
    color: black;
    font-size: 16px;
    font-weight: 600;
    padding: 14px;
    border-radius: 14px;
    border: none;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    background-color: #00cdd4;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,245,255,0.35);
}

.result {
    margin-top: 25px;
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    color: #00f5ff;
    background: rgba(0, 245, 255, 0.12);
    border: 1px solid rgba(0, 245, 255, 0.35);
}
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'>Disease Prediction System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Select symptoms and get an accurate disease prediction</div>", unsafe_allow_html=True)


with st.container():

    selected_symptoms = st.multiselect(
        "Choose Symptoms",
        symptom_columns,
        placeholder="Select one or more symptoms"
    )

    if st.button("Predict Disease"):

        if not selected_symptoms:
            st.warning("⚠️ Please select at least one symptom.")
            st.session_state.show_result = False

        else:
            st.session_state.show_result = True

            input_vector = np.zeros(len(symptom_columns))
            for symptom in selected_symptoms:
                input_vector[symptom_columns.index(symptom)] = 1

            input_df = pd.DataFrame([input_vector], columns=symptom_columns)
            probs = model.predict_proba(input_df)[0]

            top_3_idx = np.argsort(probs)[-3:][::-1]
            top_3_diseases = encoder.inverse_transform(top_3_idx)
            top_3_probs = probs[top_3_idx] * 100

            st.session_state.result_html = "<div class='result'>🩺 Top 3 Possible Diseases<br><br>"

            for disease, prob in zip(top_3_diseases, top_3_probs):
                st.session_state.result_html += f"{disease} — <b>{prob:.1f}%</b><br>"

            st.session_state.result_html += """
            <br>
            <span style='font-size:14px; opacity:0.8;'>
            ⚠️ This is an AI-based prediction. Please consult a doctor for medical advice.
            </span>
            </div>
            """


if st.session_state.show_result:
    st.markdown(st.session_state.result_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Consult a Doctor"):
        st.switch_page("pages/1_Consult_Doctor.py")













