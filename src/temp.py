import ollama

message = ollama.chat(model = 'mistral', messages = [
    {
        'role' : 'user',
        'content' : 'Why sky is blue',
    },
])

print(message['message']['content'])