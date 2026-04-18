import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate(prompt, model="phi3", temperature=0):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }
    )

    if response.status_code != 200:
        raise Exception("LLM call failed")

    return response.json()["response"]
