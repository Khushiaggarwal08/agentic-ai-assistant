from router import route_question
from judge import judge_answer
from brains.finance import generate_finance_answer
from brains.general import generate_general_answer


def run_ai(question: str) -> str:
    # 1️⃣ Route the question
    route = route_question(question)

    # 2️⃣ Generate answer based on category
    if route["category"] == "finance":
        answer = generate_finance_answer(
            question=question,
            risk=route["risk"],
            tone=route["tone"]
        )
    else:
        answer = generate_general_answer(question)

    # 3️⃣ Judge the answer
    verdict = judge_answer(answer, route["category"])

    # 4️⃣ Retry once if rejected
    if verdict["is_acceptable"]:
        return answer
    else:
        if route["category"] == "finance":
            return generate_finance_answer(
                question=question + "\n\nRewrite more clearly and conservatively.",
                risk=route["risk"],
                tone=route["tone"]
            )
        else:
            return generate_general_answer(
                question + "\n\nRewrite more clearly."
            )


if __name__ == "__main__":
    user_question = input("Ask your question: ")
    final_answer = run_ai(user_question)

    print("\nFINAL ANSWER:\n")
    print(final_answer)
