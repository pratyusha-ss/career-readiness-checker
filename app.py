import streamlit as st

st.set_page_config(
    page_title="Career Readiness Checker",
    page_icon="🎯"
)

st.title("🎯 Career Readiness Checker")
st.write("Find out how you're progressing towards your career goals!")

name = st.text_input("What is your name?")

age = st.number_input(
    "What is your age?",
    min_value=1,
    max_value=100,
    step=1
)

year = st.selectbox(
    "What school year are you in?",
    ["Year 10", "Year 11", "Year 12", "Year 13", "Other"]
)

dream_company = st.text_input("What is your dream company?")

language = st.text_input(
    "What programming languages do you know?"
)

projects = st.number_input(
    "How many projects have you completed?",
    min_value=0,
    step=1
)

github = st.selectbox(
    "Do you have a GitHub account?",
    ["Yes", "No"]
)

if st.button("Check My Readiness 🚀"):

    st.subheader("👤 Your Profile")

    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**School Year:** {year}")
    st.write(f"**Dream Company:** {dream_company}")
    st.write(f"**Programming Language:** {language}")
    st.write(f"**Projects Completed:** {projects}")
    st.write(f"**GitHub:** {github}")

    st.subheader("📊 Your Feedback")

    if projects <= 2:
        st.info("🌱 You're just getting started. Keep building projects!")
    elif projects <= 5:
        st.success("🚀 Great progress! You're building a strong portfolio.")
    else:
        st.success("🌟 Fantastic! Your portfolio is growing strong.")

    if github == "Yes":
        st.success("🐙 Excellent! Keep uploading your projects.")
    else:
        st.warning(
            "💡 Consider creating a GitHub account and sharing your projects."
        )

    st.subheader("🏆 Career Readiness Score")

    score = 0

    if projects >= 1:
        score += 1

    if projects >= 3:
        score += 1

    if github == "Yes":
        score += 1

    if language:
        score += 1

    st.metric(
        "Career Readiness Score",
        f"{score}/4"
    )
