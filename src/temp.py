import ollama

message = ollama.chat(model = 'llama2', messages = [
    {
        'role' : 'user',
        'content' : 'Why sky is blue',
    },
])

print(message['message']['content'])