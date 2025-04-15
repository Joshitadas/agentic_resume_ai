from agents.base_agent import AgenticOrchestrator
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    company = input("Enter company name: ")
    role = input("Enter job role: ")
    resume_path = "data/myResume.tex"

    agent = AgenticOrchestrator()
    agent.run(company, role, resume_path)

