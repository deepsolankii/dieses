import numpy as np
import pandas as pd
import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]


@st.cache_resource
def train_model():
    df = pd.read_csv("dataset.csv")
    scaler = StandardScaler()
    df[FEATURE_COLUMNS] = scaler.fit_transform(df[FEATURE_COLUMNS])

    model = KNeighborsClassifier(n_neighbors=8)
    model.fit(df[FEATURE_COLUMNS], df["target"])
    return model, scaler


def predict_heart_disease(values):
    model, scaler = train_model()
    user_row = np.array(values).reshape(1, len(FEATURE_COLUMNS))
    user_row = scaler.transform(user_row)
    prediction = model.predict(user_row)[0]
    return prediction


st.set_page_config(page_title="Heart Disease Predictor", layout="wide")

# Hide Streamlit header/footer and menu.
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    [data-testid="stStatusWidget"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Heart Disease Prediction")
st.write("Fill your details and click Predict.")

left_col, right_col = st.columns([1, 1.6], gap="large")

with left_col:
    age = st.number_input("Age", min_value=1, max_value=120, value=37, step=1)
    sex = st.selectbox("Sex", options=[("Female", 0), ("Male", 1)], format_func=lambda x: x[0])[1]
    cp = st.slider("Chest pain type (0-3)", min_value=0, max_value=3, value=1)
    trestbps = st.number_input("Resting blood pressure", min_value=50, max_value=250, value=120, step=1)
    chol = st.number_input("Cholesterol (mg/dl)", min_value=80, max_value=700, value=220, step=1)
    fbs = st.selectbox("Blood sugar > 120 (mg/dl)", options=[("False", 0), ("True", 1)], format_func=lambda x: x[0])[1]
    restecg = st.slider("Resting electrocardiographic (0-2)", min_value=0, max_value=2, value=1)
    thalach = st.number_input("Max heart rate", min_value=60, max_value=250, value=150, step=1)
    exang = st.selectbox("Pain during exercise", options=[("No", 0), ("Yes", 1)], format_func=lambda x: x[0])[1]
    oldpeak = st.number_input("ECG entry rate (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.slider("ECG peak slope (0-2)", min_value=0, max_value=2, value=1)
    ca = st.slider("Vessels colored by fluoroscopy (0-3)", min_value=0, max_value=3, value=0)
    thal = st.slider("Thalassemia (0-3)", min_value=0, max_value=3, value=2)

    if st.button("Predict", type="primary"):
        values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = predict_heart_disease(values)

        if prediction == 1:
            st.error("Person has a high chance of having heart disease.")
        else:
            st.success("Person has a low chance of having heart disease.")

with right_col:
    st.image("s1.jpeg", use_container_width=True)
