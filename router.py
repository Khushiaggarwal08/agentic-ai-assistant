import json
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def route_question(question: str) -> dict:
    system_prompt = """
You are a Super Router AI.

Decide ONLY:
- category
- risk
- tone

Return ONLY valid JSON.

Categories:
finance, general

Risk:
low, medium, high

Tone:
calm_professional, explanatory, analytical, neutral
"""

    try:
        response = client.chat.completions.create(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            timeout=20
        )
        return json.loads(response.choices[0].message.content.strip())

    except Exception:
        return {
            "category": "general",
            "risk": "low",
            "tone": "neutral"
        }


if __name__ == "__main__":
    q = "What is inflation?"
    print(route_question(q))
