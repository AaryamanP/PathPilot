import streamlit as st
from openai import OpenAI

#Configure Groq API Key
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" 
)

# Page config
st.set_page_config(page_title="PathPilot", page_icon="🧭", layout="centered")

# Custom CSS for navbar and styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Lato', sans-serif;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.8rem 2rem;
            background-color: #ffffff;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .navbar a {
            text-decoration: none;
            color: #333;
            font-weight: 600;
            margin-left: 1.5rem;
            transition: color 0.2s ease-in-out;
        }

        .navbar a:hover {
            color: #007BFF;
        }

        .navbar .logo {
            font-size: 1.6rem;
            font-weight: 700;
            color: #007BFF;
        }

        .navbar .nav-right {
            display: flex;
            align-items: center;
        }

        .navbar .login-btn {
            background-color: #007BFF;
            color: white !important;
            padding: 0.3rem 0.8rem;
            border-radius: 6px;
            font-weight: 600;
            margin-left: 1.5rem;
            transition: background 0.3s ease-in-out;
        }

        .navbar .login-btn:hover {
            background-color: #0056b3;
        }
    </style>

    <div class="navbar">
        <a class="logo" href="#">PathPilot</a>
        <div class="nav-right">
            <a href="#about">About Us</a>
            <a href="#login" class="login-btn">Sign Up / Log In</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Title
st.title("🎯 Inclusive Career Guidance")
st.write("Get personalized career suggestions based on your strengths, preferences, and needs.")

# Form Inputs
with st.form("career_form"):
    conditions = st.multiselect(
        "Do you have any diagnosed conditions?",
        ["Dyslexia", "Autism Spectrum", "ADHD", "Physical disability", "Other"]
    )

    activities = st.multiselect(
        "What type of activities do you enjoy most? (Pick top 2)",
        ["Working with hands", "Creative arts", "Helping/caring for people/animals",
         "Solving puzzles/math/logic problems", "Organizing or managing things",
         "Technology", "Outdoor/Nature-related activities"]
    )

    work_style = st.radio(
        "How do you prefer to work?",
        ["Alone, at my own pace", "In a small, quiet group", "In a team with clear roles", "Flexible (mix of solo & group)"]
    )

    environment = st.radio(
        "What environment suits you best?",
        ["Quiet, structured", "Active, hands-on", "Outdoors/nature", "Creative/artistic space"]
    )

    routine_preference = st.radio(
        "Do you enjoy routine or variety in tasks?",
        ["Strong routine", "Mix of routine and new tasks", "Always new challenges"]
    )

    strengths = st.multiselect(
        "What are you good at? (Pick top 3)",
        ["Attention to detail", "Creativity/artistic skills", "Problem-solving",
         "Physical coordination", "Memorizing facts/details", "Communicating", "Technology"]
    )

    learning_style = st.radio(
        "How do you learn best?",
        ["Visually", "By doing", "Listening", "Written instructions"]
    )

    challenges = st.multiselect(
        "What challenges do you face at work/school? (Pick 1-2)",
        ["Reading/writing tasks", "Social interactions", "Focusing for long periods",
         "Physical tasks", "Unstructured tasks"]
    )

    job_values = st.multiselect(
        "What’s most important in a job? (Pick top 2)",
        ["Flexibility in hours", "Clear instructions", "Helping others",
         "Creativity/freedom", "Stable income"]
    )

    career_interest = st.text_input("Any careers you’re curious about? (Optional)")

    submitted = st.form_submit_button("🔍 Get Career Suggestions")

# AI Suggestion
if submitted:
    st.info("Analyzing your answers with AI...")
    user_data = f"""
    Conditions: {', '.join(conditions)}
    Activities enjoyed: {', '.join(activities)}
    Work preference: {work_style}
    Best environment: {environment}
    Routine preference: {routine_preference}
    Strengths: {', '.join(strengths)}
    Learning style: {learning_style}
    Challenges: {', '.join(challenges)}
    Job values: {', '.join(job_values)}
    Career interests: {career_interest}
    """

    prompt = f"""
    You are a compassionate career counselor. Based on the user's strengths, preferences, and challenges, suggest 2-3 inclusive and accessible career paths. The user may have disabilities and deserves thoughtful, strengths-based guidance.

    {user_data}
    """

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=500
        )
        result = response.choices[0].message.content
        st.success("Here are some career paths you might enjoy:")
        st.markdown(result)
    except Exception as e:
        st.error(f"Error: {e}")
