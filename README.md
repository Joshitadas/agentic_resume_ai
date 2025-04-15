# Agentic Resume AI

An intelligent AI agent that customizes LaTeX resumes based on specific company values and job requirements. The system uses GPT models to analyze job requirements and enhance your resume to better match the position you're applying for.

## Features
- AI-powered company culture analysis
- Intelligent job skills extraction and matching
- Smart LaTeX resume enhancement
- Automatic keyword emphasis using \textbf{}
- Preservation of LaTeX formatting and structure
- Experience section rewriting to highlight relevant skills

## How It Works
1. **Company Analysis**: Uses GPT to understand company values and culture
2. **Skills Extraction**: Analyzes job role requirements to identify key skills
3. **Resume Enhancement**: 
   - Reorganizes skills to match job requirements
   - Emphasizes relevant technical and soft skills
   - Restructures experience descriptions
   - Adds job-specific keywords
   - Maintains professional LaTeX formatting

## Setup
1. Install dependencies:
```bash
pip install openai python-dotenv
```

2. Create a `.env` file in the project root with your OpenAI API key:
