import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="Social Media Addiction Survey",
    page_icon="📱",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.4rem;
}
.hero p { color: #a78bfa; font-size: 1rem; margin: 0; }

.section-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin: 1.2rem 0;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    color: #a78bfa;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(167,139,250,0.2);
}

.stSelectbox label, .stSlider label, .stNumberInput label {
    color: #e2e8f0 !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
}

div[data-testid="stRadio"] label {
    color: #e2e8f0 !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] {
    gap: 0.5rem;
}

div[data-testid="stRadio"] div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    padding: 0.4rem 1rem !important;
    color: #cbd5e1 !important;
    font-size: 0.88rem !important;
    font-weight: 400 !important;
    cursor: pointer;
}

div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {
    border-color: #a78bfa !important;
    background: rgba(167,139,250,0.1) !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #7c3aed, #a78bfa);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.8rem 2rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    margin-top: 1rem;
}

.progress-bar {
    background: rgba(255,255,255,0.08);
    border-radius: 99px;
    height: 6px;
    margin: 0.5rem 0 1.5rem;
    overflow: hidden;
}
.progress-fill {
    background: linear-gradient(90deg, #7c3aed, #a78bfa);
    height: 100%;
    border-radius: 99px;
}

.success-box {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.3);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1rem;
}
.success-box h2 { color: #10b981; font-family: 'Space Grotesk', sans-serif; font-size: 1.6rem; }
.success-box p { color: #a7f3d0; font-size: 0.95rem; }

.stat-chip {
    background: rgba(167,139,250,0.15);
    border: 1px solid rgba(167,139,250,0.3);
    border-radius: 99px;
    padding: 0.35rem 1rem;
    color: #c4b5fd;
    font-size: 0.82rem;
    font-weight: 500;
    display: inline-block;
    margin: 0.3rem;
}

hr { border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 1.5rem 0; }

.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(167,139,250,0.3) !important;
}
</style>
""", unsafe_allow_html=True)

CSV_FILE = "responses.csv"
COLUMNS = [
    "timestamp", "age", "gender", "occupation", "city",
    "daily_hours", "main_platform", "morning_check", "night_usage",
    "tried_to_quit", "notification_check", "study_affected",
    "anxiety_without_phone", "mood_after_use", "daily_checks",
    "sleep_hours", "self_rated_addiction"
]

def save_response(data: dict):
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_new = pd.DataFrame([data])
    if os.path.exists(CSV_FILE):
        df_existing = pd.read_csv(CSV_FILE)
        df_final = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_final = df_new
    df_final = df_final.reindex(columns=COLUMNS)
    df_final.to_csv(CSV_FILE, index=False)

def get_response_count():
    if os.path.exists(CSV_FILE):
        return len(pd.read_csv(CSV_FILE))
    return 0

if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "page" not in st.session_state:
    st.session_state.page = 1

# HERO
st.markdown("""
<div class="hero">
    <div style="font-size:3rem;">📱</div>
    <h1>Social Media Addiction Survey</h1>
    <p>A data science research project &middot; Your response stays anonymous</p>
</div>
""", unsafe_allow_html=True)

count = get_response_count()
st.markdown(f'<div style="text-align:center; margin-bottom:1.5rem;"><span class="stat-chip">🧑‍🤝‍🧑 {count} responses so far</span></div>', unsafe_allow_html=True)

# SUBMITTED
if st.session_state.submitted:
    st.markdown("""
    <div class="success-box">
        <h2>✅ Thank You!</h2>
        <p>Your response has been recorded.<br>
        This data will be used to build a social media addiction prediction model.</p>
        <div style="margin-top:1rem;">
            <span class="stat-chip">🔒 Anonymous</span>
            <span class="stat-chip">📊 Research Only</span>
            <span class="stat-chip">🤖 ML Project</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("➕ Submit Another Response"):
        st.session_state.submitted = False
        st.session_state.page = 1
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:0.8rem; text-align:center;'>Research Data</p>", unsafe_allow_html=True)
    if os.path.exists(CSV_FILE):
        df_dl = pd.read_csv(CSV_FILE)
        st.download_button(
            "⬇️ Download Dataset (CSV)",
            df_dl.to_csv(index=False),
            file_name="social_media_survey_data.csv",
            mime="text/csv"
        )
    st.stop()

# PROGRESS BAR
total_pages = 3
progress_pct = int((st.session_state.page / total_pages) * 100)
st.markdown(f"""
<div style="margin-bottom:0.3rem; color:#a78bfa; font-size:0.82rem; font-weight:500;">
    Section {st.session_state.page} of {total_pages}
</div>
<div class="progress-bar">
    <div class="progress-fill" style="width:{progress_pct}%"></div>
</div>
""", unsafe_allow_html=True)

# PAGE 1
if st.session_state.page == 1:
    st.markdown('<div class="section-card"><div class="section-title">👤 Basic Information</div>', unsafe_allow_html=True)

    age = st.number_input("Your Age", min_value=10, max_value=60, value=20, step=1)

    gender = st.selectbox("Gender", ["Select...", "Male", "Female", "Other / Prefer not to say"])

    occupation = st.selectbox("What best describes you?", [
        "Student (School)",
        "Student (University/College)",
        "Working Professional",
        "Freelancer",
        "Unemployed",
        "Other"
    ])

    city = st.selectbox("City / Province", [
        "Karachi", "Lahore", "Islamabad", "Hyderabad", "Quetta",
        "Peshawar", "Rawalpindi", "Faisalabad", "Multan", "Other"
    ])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Next →"):
        if gender == "Select...":
            st.error("Please select your gender.")
        else:
            st.session_state.p1 = {"age": age, "gender": gender, "occupation": occupation, "city": city}
            st.session_state.page = 2
            st.rerun()

# PAGE 2
elif st.session_state.page == 2:
    st.markdown('<div class="section-card"><div class="section-title">📊 Social Media Usage Habits</div>', unsafe_allow_html=True)

    daily_hours = st.selectbox("How many hours per day do you use social media?",
        ["1–2 hours", "3–4 hours", "5–6 hours", "6+ hours"])

    main_platform = st.selectbox("Which platform do you use the most?",
        ["Instagram", "TikTok", "YouTube", "Twitter / X", "Facebook", "Snapchat", "LinkedIn", "Other"])

    morning_check = st.selectbox("Do you check social media first thing in the morning?",
        ["Yes", "No", "Sometimes"])

    night_usage = st.selectbox("Do you use social media right before sleeping?",
        ["Yes, always", "Sometimes", "Rarely", "No"])

    tried_to_quit = st.selectbox("Have you ever tried to reduce social media usage and failed?",
        ["Yes", "No"])

    notification_check = st.selectbox("Do you check your phone immediately when a notification arrives?",
        ["Always", "Sometimes", "Rarely", "Never"])

    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.page = 1
            st.rerun()
    with col2:
        if st.button("Next →"):
            st.session_state.p2 = {
                "daily_hours": daily_hours, "main_platform": main_platform,
                "morning_check": morning_check, "night_usage": night_usage,
                "tried_to_quit": tried_to_quit, "notification_check": notification_check
            }
            st.session_state.page = 3
            st.rerun()

# PAGE 3
elif st.session_state.page == 3:
    st.markdown('<div class="section-card"><div class="section-title">🧠 Impact on Your Life</div>', unsafe_allow_html=True)

    study_affected = st.selectbox("Does social media negatively affect your studies or work?",
        ["Never", "Sometimes", "Often", "Always"])

    anxiety_without_phone = st.selectbox("Do you feel anxious or restless without your phone?",
        ["Yes", "No", "Sometimes"])

    mood_after_use = st.selectbox("How do you feel after using social media?",
        ["Better", "Same as before", "Worse"])

    daily_checks = st.selectbox("How many times do you check your phone per day?",
        ["1–10 times", "11–20 times", "21–30 times", "30+ times"])

    sleep_hours = st.selectbox("How many hours do you sleep per night?",
        ["Less than 5 hrs", "5–6 hrs", "7–8 hrs", "More than 8 hrs"])

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card"><div class="section-title">⭐ Self Assessment</div>', unsafe_allow_html=True)

    self_rating = st.slider(
        "Rate your own social media addiction level:",
        min_value=1, max_value=5, value=3,
        help="1 = Not addicted at all | 5 = Extremely addicted"
    )

    rating_labels = {
        1: "1 — Not addicted at all 😌",
        2: "2 — Slightly addicted 🙂",
        3: "3 — Moderately addicted 😐",
        4: "4 — Quite addicted 😟",
        5: "5 — Extremely addicted 😰"
    }
    st.markdown(f"<p style='color:#a78bfa; font-size:0.9rem; margin-top:0.3rem;'>Your rating: <strong>{rating_labels[self_rating]}</strong></p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.page = 2
            st.rerun()
    with col2:
        if st.button("✅ Submit"):
            full_response = {
                **st.session_state.p1,
                **st.session_state.p2,
                "study_affected": study_affected,
                "anxiety_without_phone": anxiety_without_phone,
                "mood_after_use": mood_after_use,
                "daily_checks": daily_checks,
                "sleep_hours": sleep_hours,
                "self_rated_addiction": self_rating
            }
            save_response(full_response)
            st.session_state.submitted = True
            st.rerun()

st.markdown("""
<hr>
<p style="text-align:center; color:#475569; font-size:0.78rem; margin-top:0.5rem;">
    Built by Shehzadi Arbab &middot; Data Science Research Project &middot; All responses are anonymous
</p>
""", unsafe_allow_html=True)