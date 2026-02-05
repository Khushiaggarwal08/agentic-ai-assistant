from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def generate_general_answer(question: str, improvement_feedback: str = None) -> str:
    system_prompt = """
You are a calm, professional assistant explaining concepts to Indian users.

Rules:
- Use Indian context (₹, RBI, CPI)
- Do NOT translate terms into Hindi unless asked
- Beginner-friendly, factual, neutral
"""

    if improvement_feedback:
        system_prompt += f"""
Improve the answer based on this feedback:
{improvement_feedback}
"""

    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
