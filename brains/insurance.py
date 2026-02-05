from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def generate_insurance_answer(question: str, improvement_feedback: str = None) -> str:
    system_prompt = """
You are a professional Indian insurance advisor.

Rules:
- Assume the user is in India
- Cover health, term, life, and general insurance
- Explain concepts simply (premium, sum assured, riders)
- Avoid recommending specific companies
- Avoid saying "best policy"
- Emphasize suitability over returns
- Mention IRDAI where relevant
"""

    if improvement_feedback:
        system_prompt += f"""
The previous answer was rejected for this reason:
{improvement_feedback}

Rewrite the answer to be clearer and more responsible.
"""

    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
