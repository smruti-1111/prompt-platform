import time
from app.schemas import ClassificationOutput
from app.utils import extract_json, build_prompt

def evaluate(prompt_template, dataset, llm_func, model="phi3"):
    correct = 0
    valid_json = 0
    total = len(dataset)
    total_latency = 0

    results = []

    for item in dataset:
        prompt = build_prompt(prompt_template, item["input"])

        start = time.time()
        raw_output = llm_func(prompt, model=model)
        latency = time.time() - start
        total_latency += latency

        try:
            parsed_json = extract_json(raw_output)
            valid_json += 1

            parsed = ClassificationOutput(**parsed_json)

            is_correct = parsed.label == item["expected"]

            if is_correct:
                correct += 1

            results.append({
                "input": item["input"],
                "expected": item["expected"],
                "output": parsed_json,
                "correct": is_correct,
                "latency": latency
            })

        except Exception as e:
            results.append({
                "input": item["input"],
                "error": str(e),
                "raw_output": raw_output
            })

    return {
        "accuracy": correct / total,
        "json_success_rate": valid_json / total,
        "avg_latency": total_latency / total,
        "details": results
    }
