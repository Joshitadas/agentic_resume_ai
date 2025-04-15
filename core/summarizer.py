import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

def summarize(content: str, prompt_type: str):
    if prompt_type == "company_values":
        prompt = f"""
Based on the following information about the company, provide a concise summary of their core values and culture:

{content}

Format the response as 3-5 key points that would be most relevant for a job application.
"""
    else:  # job_skills
        prompt = f"""
Based on the following job requirements, provide a prioritized list of the most important skills and qualifications:

{content}

Format the response as 3-5 key skills that should be emphasized in a resume.
"""

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
