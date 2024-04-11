# import ollama

# message = ollama.chat(model = 'mistral', messages = [
#     {
#         'role' : 'user',
#         'content' : 'Why sky is blue',
#     },
# ])

# print(message['message']['content'])


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