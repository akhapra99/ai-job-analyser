import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Job Description Analyser", page_icon="🎯")

# Create Claude client
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# App title
st.title("AI Job Description Analyser")
st.caption("Analyse a job description against your CV using Claude AI.")

# User inputs
cv_text = st.text_area(
    "Paste your CV here:",
    height=250
)

job_description = st.text_area(
    "Paste the job description here:",
    height=250
)

# Button
if st.button("Analyse Job Match"):

    # Validation
    if not cv_text or not job_description:
        st.warning("Please paste both your CV and the job description.")

    else:

        with st.spinner("Analysing job match..."):

            prompt = f"""
You are an expert career analyst.

Compare the candidate CV against the job description.

Return your response using this structure:

1. Match Score
Give a percentage score and explain briefly.

2. Key Skills Required
List the most important skills from the job description.

3. Candidate Strengths
Explain where the CV matches the role well.

4. Missing or Weak Areas
Explain any missing skills or weaker areas.

5. Suggested Talking Points
Give interview talking points the candidate could use.

6. CV Improvements
Suggest practical ways to improve the CV for this role.

Rules:
- Be constructive and realistic.
- Do not invent experience.
- Only use information provided.
- Keep the output clear and professional.

CV:
{cv_text}

Job Description:
{job_description}
"""

            # Claude API call
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1500,
              
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            output = response.content[0].text

        st.success("Analysis complete.")

        st.markdown(output)