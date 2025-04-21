import subprocess
from pathlib import Path

def build_modelfiles():
    i = 0
    for item in Path("models").iterdir():
        print(f"⚙️ Building model: '{item}'")
        if item.name.endswith(".ModelFile"):
            i += 1
            subprocess.run(["/usr/local/bin/ollama", "create", item.name.split(".")[0], "-f", "models/" + item.name])

    print("------")
    print(f"✅ Built {i} ModelFiles")

def get_ai_response(prompt: str, model: str) -> str:
    try:
        if not prompt: prompt = "Hello you stupid bot, I'm very clever and very funny!"
        response = subprocess.run(
            ["/usr/local/bin/ollama", "run", model, prompt], 
            capture_output=True, 
            text=True,
            check=True
        )
        print(f"Running: /usr/local/bin/ollama run {model} {prompt}")
        response_text = response.stdout.strip()
        if response_text == "":
            response_text = "I simply have no words."
        return response_text
    except subprocess.CalledProcessError as e:
        print(f"Command error: {e}")
        print(f"Error output: {e.stderr}")
        return "An error occurred while processing your request :("
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing your request :("
