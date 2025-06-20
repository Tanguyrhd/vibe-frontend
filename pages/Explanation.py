import streamlit as st

st.set_page_config(page_title="Results Explanation", layout="centered")

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
st.markdown('<div class="opaque-box"><h1>🤓 Results Explanation</h1></div>', unsafe_allow_html=True)

mbti_1 = st.session_state.get("mbti_1")
mbti_2 = st.session_state.get("mbti_2")

mbti_11 = st.session_state.get("mbti_11")
mbti_12 = st.session_state.get("mbti_12")
mbti_13 = st.session_state.get("mbti_13")
mbti_14 = st.session_state.get("mbti_14")

mbti_21 = st.session_state.get("mbti_21")
mbti_22 = st.session_state.get("mbti_22")
mbti_23 = st.session_state.get("mbti_23")
mbti_24 = st.session_state.get("mbti_24")

explanation_11 = st.session_state.get("explanation_11")
explanation_12 = st.session_state.get("explanation_12")
explanation_13 = st.session_state.get("explanation_13")
explanation_14 = st.session_state.get("explanation_14")

explanation_21 = st.session_state.get("explanation_21")
explanation_22 = st.session_state.get("explanation_22")
explanation_23 = st.session_state.get("explanation_23")
explanation_24 = st.session_state.get("explanation_24")

conf_1 = st.session_state.get("conf_1")
conf_2 = st.session_state.get("conf_2")

if not mbti_1 or not mbti_2:
    st.warning("Please start from the main page to enter tweets.")
    st.page_link("streamlit_app.py", label="← Go to Main Page")
else:
    st.markdown("""
    <div class="opaque-box">
    <span style="font-size:1.5em">
    - <b>E</b> for Extraversion  VS  <b>I</b> for Introversion <br>
    - <b>S</b> for Sensing  VS  <b>N</b> for Intuition <br>
    - <b>T</b> for Thinking  VS  <b>F</b> for Feeling <br>
    - <b>J</b> for Judging  VS  <b>P</b> for Perceiving <br>
    </span></div>
    """, unsafe_allow_html=True)

    st.subheader("Your Results")

    st.markdown(f"""<div class="green-opaque-box">
                <span style="font-size:1.5em">
                <b>Tweet from Person 1:</b> {mbti_1}""", unsafe_allow_html=True)
    st.markdown(f"""<div class="opaque-box">
                <span style="font-size:1.2em">
                <b>Why the {mbti_11} ?</b> <br>
                    {explanation_11} <br>
                    <br>
                    <b>Why the {mbti_12} ?<br> </b>
                    {explanation_12} <br>
                    <br>
                    <b>Why the {mbti_13} ?<br> </b>
                    {explanation_13} <br>
                    <br>
                    <b>Why the {mbti_14} ?<br> </b>
                    {explanation_14} <br>
                    </div>""", unsafe_allow_html=True)


    st.markdown(f"""<div class="green-opaque-box">
                <span style="font-size:1.5em">
                <b>Tweet from Person 2:</b> {mbti_2}""", unsafe_allow_html=True)
    st.markdown(f"""<div class="opaque-box">
                <span style="font-size:1.2em">
                <b>Why the {mbti_21} ?</b> <br>
                {explanation_21} <br>
                <br>
                <b>Why the {mbti_22} ?<br> </b>
                {explanation_22} <br>
                <br>
                <b>Why the {mbti_23} ?<br> </b>
                {explanation_23} <br>
                <br>
                <b>Why the {mbti_24} ?<br> </b>
                {explanation_24} <br>
                </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f'<div class="blue-opaque-box"><b> SEE COMPATIBILITY </b>', unsafe_allow_html=True)
    st.page_link("pages/1_🤝_Compatibility_Results.py", label="➡️ CLICK HERE")
