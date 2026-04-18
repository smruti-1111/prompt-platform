import json
import re

def extract_json(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("Invalid JSON")

def build_prompt(template, user_input):
    return template.replace("{input}", user_input)
