from fastapi import FastAPI
import json
import os
from datetime import datetime

from app.prompt_manager import load_prompt
from app.evaluator import evaluate
from app.llm import generate

app = FastAPI()

DATASET_PATH = "data/dataset.json"
RESULTS_DIR = "results"

@app.get("/")
def home():
    return {"message": "Prompt Platform Running"}

@app.get("/evaluate/{version}")
def run_evaluation(version: str, model: str = "phi3"):
    prompt = load_prompt(version)

    with open(DATASET_PATH, "r") as f:
        dataset = json.load(f)

    result = evaluate(prompt, dataset, generate, model=model)

    os.makedirs(RESULTS_DIR, exist_ok=True)

    filename = f"{version}_{model}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(os.path.join(RESULTS_DIR, filename), "w") as f:
        json.dump(result, f, indent=2)

    return result
