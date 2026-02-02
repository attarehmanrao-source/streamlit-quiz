import streamlit as st
st.title("Quiz Game")
score = 0
q1 = st.radio(
    "1) pakistan ka sab se bada city konsa hai?",
    ["karachi", "lahore", "multan"],
    index=None
)
if q1 == "karachi":
    score += 1
    q2 = st.radio(
        "2) pakistan kis saal aazad hua tha?",
        ["1944", "1945","1947"],
        index=None
    )
if q2 == "1947":
        score += 1
        if st.button("submit"):
            if q1 is None or q2 is None:
                st.warning("please donon sawalon ka jawab den")
            else:
                st.success(f"aap ka score: {score} / 2")