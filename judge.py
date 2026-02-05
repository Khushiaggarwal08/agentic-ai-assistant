import json
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def judge_answer(answer: str, category: str) -> dict:
    system_prompt = """
You are an extremely strict evaluator.

Reject answers that are:
- Generic
- Unsafe
- Misleading
- Poorly structured

Respond ONLY in JSON:
{
  "is_acceptable": true/false,
  "feedback": "reason"
}
"""

    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": answer}
        ]
    )

    return json.loads(response.choices[0].message.content)
