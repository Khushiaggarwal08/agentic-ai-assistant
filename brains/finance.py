from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def generate_finance_answer(question: str, risk: str, tone: str) -> str:
    base = """
You are a calm, professional finance assistant for an Indian audience.

Rules:
- No buy/sell advice
- No return guarantees
- No fear or urgency
- Use Indian context (₹, RBI, SIP, FD, bonds)
- Help the user think, not act
"""

    if tone == "explanatory":
        style = "Explain simply. Assume the user is a beginner."
    elif tone == "analytical":
        style = "Explain with reasoning and trade-offs."
    else:
        style = "Be neutral and professional."

    if risk == "high":
        caution = "Be extra cautious. Add clear limitations."
    else:
        caution = "Maintain a balanced tone."

    system_prompt = f"""
{base}

STYLE:
{style}

RISK:
{caution}
"""

    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
