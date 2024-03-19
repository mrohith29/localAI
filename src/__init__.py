from argparse import Namespace, ArgumentParser
import ollama
from rich.console import Console

def hey():
    
    console = Console()
    # parser = ArgumentParser(description='Communicate with AI locally')
    # parser.add_argument('-m', '--message', type=str, required=True, help="type -m or --message to tell the cli that you have a question to ask")
    # parser.add_argument('message', type=str, required=True, help="Question you want to ask")

    # args = parser.parse_args()
    # respond = ollama.ask(args.message)
    # console.print(respond)

    responce = ollama.chat(model='llama2', messages=[
        {
            'role' : 'user',
            'content': 'Why sky is blue',
        },
    ])
    console.print(responce['message']['content'])
if __name__ == "__main__":
    hey()