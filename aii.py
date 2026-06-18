import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.title("AI Resume Analyzer")

resume_text = st.text_area(
    "Paste your resume here",
    height=300
)

if st.button("Analyze Resume"):

    if resume_text.strip() == "":
        st.warning("Please paste your resume first.")
    else:

        with st.spinner("Analyzing..."):

            response = client.responses.create(
                model="gpt-5",
                input=f"""
                Analyze this resume.

                Give:
                1. Strengths
                2. Weaknesses
                3. Missing skills
                4. Suggestions for improvement
                5. Overall score out of 10

                Resume:
                {resume_text}
                """
            )

            st.subheader("Analysis")
            st.write(response.output_text)