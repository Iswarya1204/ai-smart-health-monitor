import streamlit as st

# -------------------------------------------------
# AI SMART HEALTH MONITOR
# Academic Demonstration Prototype
# -------------------------------------------------

st.set_page_config(
    page_title="AI Smart Health Monitor",
    page_icon="🏥",
    layout="centered"
)

# -------------------------------------------------
# CUSTOM DESIGN
# -------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #172554, #312e81);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.metric-card {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 15px;
    text-align: center;
}

.metric-name {
    font-size: 18px;
    color: #cbd5e1;
}

.metric-value {
    font-size: 36px;
    font-weight: 700;
    margin-top: 5px;
}

.result-box {
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    margin-top: 25px;
}

.normal {
    background: #14532d;
    border: 2px solid #4ade80;
}

.warning {
    background: #78350f;
    border: 2px solid #fbbf24;
}

.danger {
    background: #7f1d1d;
    border: 2px solid #f87171;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.markdown(
    '<div class="main-title">🏥 AI Smart Health Monitor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Based Smart Health Monitoring & Emergency Alert System'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the patient's health readings below. "
    "The prototype analyzes the readings and classifies the current risk level."
)

st.divider()

# -------------------------------------------------
# INPUT SECTION
# -------------------------------------------------

st.subheader("📊 Enter Health Readings")

col1, col2 = st.columns(2)

with col1:
    heart_rate = st.number_input(
        "❤️ Heart Rate (BPM)",
        min_value=30,
        max_value=220,
        value=82,
        step=1
    )

with col2:
    spo2 = st.number_input(
        "🫁 SpO₂ (%)",
        min_value=50,
        max_value=100,
        value=98,
        step=1
    )

temperature = st.number_input(
    "🌡️ Temperature (°C)",
    min_value=30.0,
    max_value=45.0,
    value=36.7,
    step=0.1,
    format="%.1f"
)

st.divider()

# -------------------------------------------------
# ANALYSIS FUNCTION
# -------------------------------------------------

def analyze_health(heart_rate, spo2, temperature):

    risk_points = 0
    warnings = []

    # Heart rate
    if heart_rate < 50 or heart_rate > 120:
        risk_points += 2
        warnings.append("Heart rate is outside the prototype's normal range.")
    elif heart_rate < 60 or heart_rate > 100:
        risk_points += 1
        warnings.append("Heart rate is slightly outside the typical resting range.")

    # SpO2
    if spo2 < 90:
        risk_points += 3
        warnings.append("SpO₂ is critically low in this prototype.")
    elif spo2 < 95:
        risk_points += 2
        warnings.append("SpO₂ is below the prototype's normal range.")

    # Temperature
    if temperature >= 39.0 or temperature < 35.0:
        risk_points += 3
        warnings.append("Temperature is significantly outside the prototype's normal range.")
    elif temperature >= 38.0 or temperature < 36.0:
        risk_points += 2
        warnings.append("Temperature is outside the prototype's normal range.")

    # Classification
    if risk_points >= 4:
        return "HIGH RISK", "danger", warnings

    elif risk_points >= 2:
        return "WARNING", "warning", warnings

    else:
        return "NORMAL", "normal", warnings


# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------

if st.button("🤖 Analyze Health", use_container_width=True):

    status, box_class, warnings = analyze_health(
        heart_rate,
        spo2,
        temperature
    )

    st.subheader("📋 Health Analysis")

    # Display readings
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-name">❤️ Heart Rate</div>
                <div class="metric-value">{heart_rate} BPM</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-name">🫁 SpO₂</div>
                <div class="metric-value">{spo2}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-name">🌡️ Temperature</div>
                <div class="metric-value">{temperature:.1f} °C</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------
    # RESULT
    # -------------------------------------------------

    if status == "NORMAL":

        st.markdown(
            """
            <div class="result-box
