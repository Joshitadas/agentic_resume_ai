import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()  # Create client instance

def read_latex_file(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def write_latex_file(path: str, content: str):
    with open(path, 'w') as file:
        file.write(content)

def rewrite_resume_with_emphasis(resume_path: str, skills: str, job_role: str) -> str:
    latex_content = read_latex_file(resume_path)

    prompt = f"""
You are an expert resume editor skilled in LaTeX formatting and career consulting.

Your task:
- Enhance the following LaTeX resume for the job role: **{job_role}**
- Emphasize key skills: {skills}
- Rewrite or rephrase resume content to highlight the skills naturally.
- Use \textbf{{}} for relevant keywords.
- Keep LaTeX formatting clean and valid.
- Do not add imaginary experiences.

Here is the LaTeX resume:
```latex
{latex_content}
```

Return only the updated LaTeX.
"""

    print("🤖 Sending resume to LLM for enhancement...")
    try:
        response = client.chat.completions.create(  # Updated to new API syntax
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        enhanced_resume = response.choices[0].message.content.strip()
        output_path = "outputs/updated_resume.tex"
        write_latex_file(output_path, enhanced_resume)
        print(f"✅ Enhanced resume saved to: {output_path}")
        return enhanced_resume

    except Exception as e:
        print(f"❌ Error during LLM resume enhancement: {e}")
        return ""