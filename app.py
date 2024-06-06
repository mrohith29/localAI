import requests
from flask import Flask, render_template, request, Response, stream_with_context
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        question = request.form.get('question')
        return render_template('index.html', quest=question)
    return render_template('index.html')

@app.route('/stream')
def stream():
    question = request.args.get('question')
    data = {
        "model": "orca-mini",
        # "model": "mistral",
        "prompt": str(question)
    }

    @stream_with_context
    def generate():
        with requests.post("http://127.0.0.1:11434/api/generate", json=data, stream=True) as response:
            if response.headers.get('Content-Type') == 'application/x-ndjson':
                for line in response.iter_lines():
                    if line:
                        resp = json.loads(line)
                        if 'response' in resp:
                            chunk = resp['response']
                            yield f"data: {chunk}\n\n"

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
