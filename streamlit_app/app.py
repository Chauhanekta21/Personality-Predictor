from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "personality_dataset.csv"
EXCLUDED_FEATURES = {"personality_type", "emotional_stability", "stress_handling", "creativity"}
FEATURE_GROUPS = {
    "Social Profile": [
        "social_energy",
        "alone_time_preference",
        "talkativeness",
        "group_comfort",
        "party_liking",
        "listening_skill",
        "empathy",
        "friendliness",
    ],
    "Thinking & Work Style": [
        "deep_reflection",
        "organization",
        "leadership",
        "public_speaking_comfort",
        "curiosity",
        "planning",
        "work_style_collaborative",
        "decision_speed",
    ],
    "Lifestyle & Preferences": [
        "risk_taking",
        "routine_preference",
        "excitement_seeking",
        "spontaneity",
        "adventurousness",
        "reading_habit",
        "sports_interest",
        "online_social_usage",
        "travel_desire",
        "gadget_usage",
    ],
}
FEATURE_LABELS = {
    feature: feature.replace("_", " ").title()
    for feature_group in FEATURE_GROUPS.values()
    for feature in feature_group
}

st.set_page_config(
    page_title="Personality Predictor",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --ink: #17242b;
        --muted: #64747b;
        --paper: #f7f8f3;
        --panel: #ffffff;
        --mint: #d9eee4;
        --teal: #176b67;
        --coral: #e9785b;
        --line: #dce5df;
    }

    .stApp {
        background: linear-gradient(135deg, #f7f8f3 0%, #edf5ee 55%, #fff8ef 100%);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    .block-container {
        max-width: 1120px;
        padding: 3.5rem 2rem 4rem;
    }

    h1, h2, h3 {
        color: var(--ink);
        font-family: 'Space Grotesk', sans-serif;
        letter-spacing: 0;
    }

    h1 {
        font-size: clamp(2.5rem, 6vw, 5.2rem);
        font-weight: 700;
        letter-spacing: -0.035em;
        line-height: 0.98;
        margin: 0;
        max-width: 820px;
    }

    .hero-title span {
        background: linear-gradient(100deg, var(--teal), var(--coral));
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        display: inline-block;
    }

    .eyebrow {
        color: var(--coral);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .intro {
        color: var(--muted);
        font-size: 1.08rem;
        line-height: 1.65;
        max-width: 650px;
        margin-bottom: 2.4rem;
    }

    .section-title {
        border-bottom: 1px solid var(--line);
        margin: 2.3rem 0 1.1rem;
        padding-bottom: 0.65rem;
    }

    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 0.8rem 1.4rem 1.4rem;
    }

    div[data-testid="stSlider"] label {
        color: var(--ink);
        font-weight: 600;
    }

    .result {
        background: var(--teal);
        border-radius: 14px;
        color: white;
        margin: 2rem 0 0.8rem;
        padding: 1.6rem 1.8rem;
    }

    .result-label {
        color: #bfe2d7;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }

    .result-value {
        color: white;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2rem, 6vw, 4rem);
        font-weight: 700;
        line-height: 1.05;
        margin-top: 0.35rem;
    }

    .note {
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.5;
        margin-top: 1rem;
    }

    button[kind="primary"] {
        background: var(--coral) !important;
        border: 0 !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: 700 !important;
        min-height: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    if "personality_type" not in data.columns:
        raise ValueError("The dataset must contain a personality_type column.")
    return data


@st.cache_resource
def train_model():
    data = load_data()
    feature_columns = [column for column in data.columns if column not in EXCLUDED_FEATURES]
    target_encoder = LabelEncoder()
    target = target_encoder.fit_transform(data["personality_type"])
    model = LogisticRegression(max_iter=1000)
    model.fit(data[feature_columns], target)
    return model, target_encoder, feature_columns


try:
    model, target_encoder, feature_columns = train_model()
except Exception as error:
    st.error(f"The predictor could not be loaded: {error}")
    st.stop()

st.markdown('<div class="eyebrow">Personality Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<h1 class="hero-title">Find the personality pattern<br><span>behind your answers.</span></h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="intro">Rate each statement from 0 to 10. Your responses will help the model identify your personality type — whether you’re an Introvert, Extrovert, or Ambivert.</p>',
    unsafe_allow_html=True,
)

with st.form("personality_form"):
    input_values = {}
    for group_name, group_features in FEATURE_GROUPS.items():
        st.markdown(f'<h2 class="section-title">{group_name}</h2>', unsafe_allow_html=True)
        columns = st.columns(2)
        for index, feature in enumerate(group_features):
            with columns[index % 2]:
                input_values[feature] = st.slider(
                    FEATURE_LABELS[feature],
                    min_value=0,
                    max_value=10,
                    value=5,
                    step=1,
                    help="0 means very low and 10 means very high.",
                )

    submitted = st.form_submit_button("Check my personality type", type="primary", use_container_width=True)

if submitted:
    input_frame = pd.DataFrame([{feature: input_values[feature] for feature in feature_columns}])
    prediction = model.predict(input_frame)[0]
    personality_type = target_encoder.inverse_transform([prediction])[0]
    st.markdown(
        f'<div class="result"><div class="result-label">Your personality type</div><div class="result-value">{personality_type}</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='note'>This result is a model prediction based on the answers provided, not a clinical or psychological diagnosis.</div>",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<div class="note">Complete the profile above to receive your predicted personality type.</div>',
        unsafe_allow_html=True,
    )
