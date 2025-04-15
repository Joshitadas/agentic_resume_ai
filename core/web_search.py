import os
from openai import OpenAI
from typing import List, Dict

client = OpenAI()

def search_web(query: str) -> List[Dict[str, str]]:
    """
    Use ChatGPT to generate information about companies or job roles.
    Returns a list of dictionaries containing relevant information.
    """
    if "core values" in query.lower():
        prompt = f"""
Provide a detailed analysis of {query.replace('core values site:', '')}'s company culture and values.
Focus on:
1. Core values and principles
2. Company culture highlights
3. Mission and vision
4. Work environment and practices

Format the response as a bulleted list with clear, concise points.
"""
    else:  # job skills query
        prompt = f"""
Provide a comprehensive list of skills and requirements for the role: {query.replace('required skills', '')}.
Focus on:
1. Essential technical skills
2. Required soft skills
3. Key responsibilities
4. Preferred qualifications

Format the response as a bulleted list with clear, concise points.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        content = response.choices[0].message.content.strip()
        points = [line.strip() for line in content.split('\n') if line.strip() and line.strip().startswith('-')]
        
        return [{"snippet": point[2:].strip()} for point in points]  # Remove the bullet point

    except Exception as e:
        print(f"⚠️ Warning: ChatGPT API error: {e}. Using placeholder results.")
        return [
            {"snippet": f"Could not retrieve information for {query}. Please try again."}
        ]
