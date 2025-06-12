import streamlit as st
import requests
from function import classify_personality

st.set_page_config(page_title="MBTI Predictor", layout="centered")

# Inject background image and opaque box style, plus green opaque box style
st.markdown(
    """
<style>
.stApp {
    background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                      url("https://daoinsights.com/wp-content/webp-express/webp-images/uploads/2022/04/mbti-types.png.webp");
    background-size: contain;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}

/* Style for dark opaque content boxes */
.opaque-box {
    background-color: rgba(0, 0, 0, 0.75);
    padding: 1.5rem;
    border-radius: 15px;
    margin-bottom: 1.5rem;
    color: white !important;
}

/* Style for green opaque result boxes */
.green-opaque-box {
    background-color: rgba(0, 128, 0, 0.7);
    padding: 1.2rem;
    border-radius: 12px;
    color: white !important;
    margin-bottom: 1rem;
}

/* Style for blue opaque result boxes */
.blue-opaque-box {
    background-color: rgba(0, 123, 255, 0.7);  /* Bootstrap primary blue with opacity */
    padding: 1.2rem;
    border-radius: 12px;
    color: white !important;
    margin-bottom: 1rem;
}

.description-caption {
    font-size: 1.1rem;
    font-weight: 600;
    color: white !important;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    margin-top: 0.25rem;
}



/* Force white text for all content */
html, body, .stApp, .opaque-box, .green-opaque-box, h1, h2, h3, h4, h5, h6, p, span, div, a {
    color: white !important;
}
</style>
    """,
    unsafe_allow_html=True
)

# Title & Description
st.markdown('<div class="opaque-box"><h1>🧠 Project Vibes: MBTI Tweet Classifier</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="opaque-box">Paste <b>two tweets</b> from different people and we\'ll predict their personalities.</div>', unsafe_allow_html=True)

# Initialize session state
if "tweet1" not in st.session_state:
    st.session_state["tweet1"] = ""
if "tweet2" not in st.session_state:
    st.session_state["tweet2"] = ""

# Inputs
col1, col2 = st.columns(2)
with col1:
    tweet1 = st.text_area("Tweet from one person", value=st.session_state["tweet1"], key="input1")
with col2:
    tweet2 = st.text_area("Tweet from another person", value=st.session_state["tweet2"], key="input2")

if st.button("Get MBTI Results"):
    if tweet1 and tweet2:
        try:

            res1 = classify_personality(tweet1)
            res2 = classify_personality(tweet2)

            mbti_11 = res1["EI"]["letter"]
            st.session_state["mbti_11"] = mbti_11
            mbti_12 = res1["SN"]["letter"]
            st.session_state["mbti_12"] = mbti_12
            mbti_13 = res1["TF"]["letter"]
            st.session_state["mbti_13"] = mbti_13
            mbti_14 = res1["JP"]["letter"]
            st.session_state["mbti_14"] = mbti_14

            conf_11 = res1["EI"]["confidence"]
            conf_12 = res1["SN"]["confidence"]
            conf_13 = res1["TF"]["confidence"]
            conf_14 = res1["JP"]["confidence"]
            conf_1 = (conf_11 + conf_12 + conf_13 + conf_14)/4
            st.session_state["conf_1"] = conf_1

            explanation_11 = res1["EI"]["explanation"]
            st.session_state["explanation_11"] = explanation_11
            explanation_12 = res1["SN"]["explanation"]
            st.session_state["explanation_12"] = explanation_12
            explanation_13 = res1["TF"]["explanation"]
            st.session_state["explanation_13"] = explanation_13
            explanation_14 = res1["JP"]["explanation"]
            st.session_state["explanation_14"] = explanation_14

            mbti_21 = res2["EI"]["letter"]
            st.session_state["mbti_21"] = mbti_21
            mbti_22 = res2["SN"]["letter"]
            st.session_state["mbti_22"] = mbti_22
            mbti_23 = res2["TF"]["letter"]
            st.session_state["mbti_23"] = mbti_23
            mbti_24 = res2["JP"]["letter"]
            st.session_state["mbti_24"] = mbti_24

            conf_21 = res2["EI"]["confidence"]
            conf_22 = res2["SN"]["confidence"]
            conf_23 = res2["TF"]["confidence"]
            conf_24 = res2["JP"]["confidence"]
            conf_2 = (conf_21 + conf_22 + conf_23 + conf_24)/4
            st.session_state["conf_2"] = conf_2

            explanation_21 = res2["EI"]["explanation"]
            st.session_state["explanation_21"] = explanation_21
            explanation_22 = res2["SN"]["explanation"]
            st.session_state["explanation_22"] = explanation_22
            explanation_23 = res2["TF"]["explanation"]
            st.session_state["explanation_23"] = explanation_23
            explanation_24 = res2["JP"]["explanation"]
            st.session_state["explanation_24"] = explanation_24


            st.session_state["tweet1"] = tweet1
            st.session_state["tweet2"] = tweet2
            st.session_state["mbti_1"] = mbti_11 + mbti_12 + mbti_13 + mbti_14
            st.session_state["mbti_2"] = mbti_21 + mbti_22 + mbti_23 + mbti_24


            st.markdown('<div class="opaque-box"><h3>🧠 Predictions</h3></div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            # conf_1 = "87%"
            # conf_2 = "91%"
            with col1:
                st.markdown(f"""<div class="green-opaque-box">
                            <span style="font-size:1.5em">
                            <b>Tweet from Person 1:</b> {mbti_11 + mbti_12 + mbti_13 + mbti_14} <br>
                            with a confidence of {conf_1}%</div>""", unsafe_allow_html=True)

            with col2:
                st.markdown(f"""<div class="green-opaque-box">
                            <span style="font-size:1.5em">
                            <b>Tweet from Person 2:</b> {mbti_21 + mbti_22 + mbti_23 + mbti_24} <br>
                            with a confidence of {conf_2}%</div>""", unsafe_allow_html=True)

            st.markdown("---")

            st.markdown(f'<div class="blue-opaque-box"><b> SEE COMPATIBILITY </b>', unsafe_allow_html=True)
            st.page_link("pages/1_🤝_Compatibility_Results.py", label="➡️ CLICK HERE")

            st.markdown(f'<div class="blue-opaque-box"><b> SEE EXPLANATION </b>', unsafe_allow_html=True)
            st.page_link("pages/Explanation.py", label="➡️ CLICK HERE")

        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter both tweets.")
