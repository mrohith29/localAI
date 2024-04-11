import requests
import json

data = {
    "model": "mistral",
    "prompt": "Why sky is blue"
}

response = requests.post("http://127.0.0.1:11434/api/generate", json=data, stream=True)
for line in response.iter_lines():
    if line:
        json_data = json.loads(line)
        if json_data["done"] == False:
            print(json_data["response"], end="", flush=True)