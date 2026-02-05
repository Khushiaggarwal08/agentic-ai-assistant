from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def generate_tax_answer(question: str, improvement_feedback: str = None) -> str:
    system_prompt = """
You are a senior Indian tax advisor writing for a professional finance website.

This content must be conservative, legally safe, and suitable for public users.

ABSOLUTE RULES:
- Never mention gender, marriage, or male/female eligibility
- Never claim HUF automatically saves tax
- Never claim HUF avoids clubbing provisions
- Never claim exemptions by default
- Never mention inheritance or succession benefits
- Never mention registrar of companies or registration authorities
- Never use persuasive or sales language

FACTUAL BOUNDARIES:
- HUF is a separate taxable entity under Indian income-tax law
- HUF requires only:
  • PAN in the name of HUF
  • Bank account in the name of HUF
- Tax treatment depends on income source and applicable provisions
- Salary income cannot be routed through HUF

MANDATORY STRUCTURE:
1. What HUF is
2. Clear statement that HUF does NOT automatically save tax
3. When HUF may help (limited cases)
4. When HUF may not help
5. Clear caution

STYLE:
- Neutral
- Professional
- Website-ready
"""

    if improvement_feedback:
        system_prompt += f"""
The earlier response was unsafe for public use:
{improvement_feedback}

Rewrite strictly within the rules.
"""

    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
