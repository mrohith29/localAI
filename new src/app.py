from flask import Flask, render_template, request
from transformers import GPT2Tokenizer, GPTNeoForCausalLM
from waitress import serve

app = Flask(__name__)
app.config['ENV'] = 'production'

# Load model
model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTNeoForCausalLM.from_pretrained(model_name)

# Set maximum length for generated tokens
max_length = 200

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/generate', methods=['POST'])
def generate_response():
    if request.method == 'POST':
        question = request.form['question']
        # Tokenize input question
        input_ids = tokenizer.encode(question, return_tensors='pt')
        # Generate response
        output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
        # Decode generated tokens to text
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return render_template('index.html', question=question, response=response)

if __name__ == '__main__':
    # app.run(debug=True)
     serve(app, host='127.0.0.1', port=5000)



# from flask import Flask, render_template, request
# import ollama

# app = Flask(__name__)

# # Home page route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Route to handle form submission
# @app.route('/generate', methods=['POST'])
# def generate_response():
#     if request.method == 'POST':
#         question = request.form['question']
#         # Generate response
#         message = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': question}])
#         response = message['message']['content']
#         return render_template('index.html', question=question, response=response)

# if __name__ == '__main__':
#     app.run(debug=True)