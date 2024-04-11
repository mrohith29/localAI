import requests
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.get('/api/<question>')
def generate_response(question):
    print(question)
    data = {
        "model": "orca-mini",
        "prompt": str(question)
    }

    print("Received question, processing answer")

    response = requests.post("http://127.0.0.1:11434/api/generate", json=data, stream=False)

    # return jsonify(response.text)
    # print(response)

    # print the status code
    print(response.status_code)

    # print the response headers
    # print(response.headers)

    # print the response body as text
    print(response.text)

    # if 'application/x-ndjson' in response.headers.get('Content-Type'):
    #     lines = response.text.splitlines()
    #     response = [json.loads(line) for line in lines if line]
    #     paragraph = "".join([resp['response'] for resp in response if 'response' in resp])
        # print(paragraph)

        # return render_template('index.html', quest = question, resp = response)

    # If the response is JSON, you can decode it into a Python object
    if 'json' in response.headers.get('Content-Type'):
        data = response.json()
        print(data)
if __name__ == '__main__':
    # app.run(debug=True)
    generate_response("why the sky is blue?")