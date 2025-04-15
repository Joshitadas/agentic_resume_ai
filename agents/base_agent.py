import os
from openai import OpenAI
from agents.tools import TOOLS
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

class AgenticOrchestrator:
    def __init__(self):
        self.state = {}

    def run(self, company: str, role: str, resume_path: str):
        self.state['company'] = company
        self.state['role'] = role
        self.state['resume_path'] = resume_path

        print("\n🤖 Invoking agent to determine action...")
        plan = self.plan_next_step()

        for tool_call in plan:
            tool_name = tool_call['tool']
            print(f"\n🛠️ Executing tool: {tool_name}")

            if tool_name == "search_company_values":
                self.state['values'] = TOOLS[tool_name]['function'](company)
            elif tool_name == "get_job_skills":
                self.state['skills'] = TOOLS[tool_name]['function'](role)
            elif tool_name == "update_resume":
                TOOLS[tool_name]['function']({
                    "resume_path": resume_path,
                    "skills": self.state['skills'],
                    "role": role
                })
                self.state['resume_updated'] = True

        print("\n✅ Agent workflow completed.")

    def plan_next_step(self):
        tools_schema = [
            {"tool": name, "description": tool['description']} for name, tool in TOOLS.items()
        ]

        plan_prompt = f"""
You are an intelligent AI orchestrator. Based on the following goal, determine the order of tool usage.

Goal: Improve a LaTeX resume for the role '{self.state['role']}' at company '{self.state['company']}'.

Available tools:
{tools_schema}

Return a list of tool names in order as a plan.
"""

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": plan_prompt}]
        )

        plan = response.choices[0].message.content.strip()

        return [
            {"tool": tool_name.strip()} for tool_name in eval(plan)
        ]
