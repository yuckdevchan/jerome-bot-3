import subprocess, random
from pathlib import Path

from config import config

def build_model_files() -> list:
    models = []
    i = 0
    for item in Path("models").iterdir():
        print(f"⚙️ Building model: '{item}'")
        if item.name.endswith(".ModelFile"):
            models.append(item.name.split(".")[0])
            i += 1
            subprocess.run(["/usr/local/bin/ollama", "create", item.name.split(".")[0], "-f", "models/" + item.name])
    print("------")
    print(f"✅ Built {i} ModelFiles")
    return models

def get_ai_response(prompt: str, model: str) -> str:
    try:
        if not prompt: prompt = "I don't care about you."
        response = subprocess.run(
            ["/usr/local/bin/ollama", "run", model, prompt], 
            capture_output=True, 
            text=True,
            check=True
        )
        response_text = response.stdout.strip()
        if response_text == "":
            response_text = "I simply have no words."
        if model.endswith("_angry"):
            response_text = response_text.upper()
        return response_text
    except subprocess.CalledProcessError as e:
        print(f"Command error: {e}")
        print(f"Error output: {e.stderr}")
        return config["speechless"]
    except Exception as e:
        print(f"Error: {e}")
        return config["speechless"]
