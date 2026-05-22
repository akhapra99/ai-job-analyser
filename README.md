\# Job Description Analyser

\### AI-powered CV and job description matching tool



Paste a job description and your CV — get an instant match score, skill gap analysis, and tailored interview talking points. Built with Python, Streamlit, and the Claude API.



\---



\## What it does



Job applications are a guessing game. This tool removes the guesswork by giving you a clear, honest picture of how well you match a role — and exactly what to say in the interview to maximise your chances.



\*\*Input:\*\* Your CV + a job description  

\*\*Output:\*\* A structured analysis in seconds



\---



\## Features



\- \*\*Match score\*\* — percentage score with an honest assessment of your fit

\- \*\*Key skills required\*\* — what the employer is actually looking for

\- \*\*Candidate strengths\*\* — where your experience clearly matches the role

\- \*\*Gaps to address\*\* — missing or weak areas to be aware of before applying

\- \*\*Interview talking points\*\* — specific things to say, grounded in your real experience

\- \*\*CV improvements\*\* — practical suggestions to tailor your CV for this specific role



\---



\## Tech stack



\- \*\*Python\*\* — core application logic

\- \*\*Streamlit\*\* — web UI

\- \*\*Anthropic Claude API\*\* (claude-sonnet-4-5) — analysis engine

\- \*\*python-dotenv\*\* — secure API key management



\---



\## Setup \& installation



\*\*1. Clone the repository\*\*

```bash

git clone https://github.com/YOUR\_USERNAME/job-description-analyser.git

cd job-description-analyser

```



\*\*2. Install dependencies\*\*

```bash

pip install -r requirements.txt

```



\*\*3. Add your Anthropic API key\*\*



Create a `.env` file in the root directory:

```

ANTHROPIC\_API\_KEY=your\_api\_key\_here

```



Get your API key at \[console.anthropic.com](https://console.anthropic.com)



\*\*4. Run the app\*\*

```bash

streamlit run app.py

```



The app will open in your browser at `http://localhost:8501`



\---



\## Usage



1\. Paste your CV into the left text box

2\. Paste the full job description into the right text box

3\. Click \*\*Analyse Job Match\*\*

4\. Review your match score, gaps, and talking points

5\. Tailor your application and prep your interview accordingly



\---



\## Project structure



```

job-description-analyser/

├── app.py               # Main Streamlit application

├── requirements.txt     # Dependencies

├── env\_example.env      # Example environment file

├── .gitignore           # Keeps your API key out of GitHub

└── README.md

```



\---



\## Requirements



```

streamlit

anthropic

python-dotenv

```



\---



\## Key design decisions



\- \*\*Single prompt, structured output\*\* — one well-engineered prompt returns all six sections in a consistent format, keeping latency low and output predictable

\- \*\*Low temperature (0.3)\*\* — keeps analysis grounded and factual rather than creative or embellished

\- \*\*Constructive framing\*\* — the prompt explicitly instructs the model not to invent experience, keeping output honest and useful

\- \*\*Streamlit for speed\*\* — zero frontend overhead means the tool can be built, iterated, and deployed fast



\---



\## Author



\*\*Ayush Khapra\*\*  

Data Analyst \& AI Engineer  

\[LinkedIn](https://www.linkedin.com/in/ayush-khapra-1227051ba/) | \[GitHub](https://github.com/akhapra99)



\---



\*Part of a portfolio of AI and data projects — May 2026\*

