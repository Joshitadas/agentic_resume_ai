from core import web_search, summarizer, latex_editor

TOOLS = {
    "search_company_values": {
        "description": "Search the company's website and summarize its core values.",
        "function": lambda company: summarizer.summarize(
            " ".join([res['snippet'] for res in web_search.search_web(f'{company} core values site:{company}.com')]),
            prompt_type="company_values"
        )
    },
    "get_job_skills": {
        "description": "Search job sites and extract core technical and soft skills for the specified role.",
        "function": lambda role: summarizer.summarize(
            " ".join([res['snippet'] for res in web_search.search_web(f'{role} required skills')]),
            prompt_type="job_skills"
        )
    },
    "update_resume": {
        "description": "Use an LLM to rewrite LaTeX resume content, emphasizing skills relevant to the job role.",
        "function": lambda args: latex_editor.rewrite_resume_with_emphasis(
            resume_path=args['resume_path'],
            skills=args['skills'],
            job_role=args['role']
        )
    }
}