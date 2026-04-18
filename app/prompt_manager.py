import os

PROMPT_DIR = "prompts"

def load_prompt(version):
    path = os.path.join(PROMPT_DIR, f"{version}.txt")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt {version} not found")

    with open(path, "r") as f:
        return f.read()
