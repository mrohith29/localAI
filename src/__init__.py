from argparse import Namespace, ArgumentParser
import ollama

def run():

    parser = ArgumentParser(description='Communicate with AI locally')
    parser.add_argument('-m', '--message', type=str, required=True, help="type -m or --message to tell the cli that you have a question to ask")
    parser.add_argument('message', type=str, required=True, help="Question you want to ask")

    args = parser.parse_args()
    print(args.message)

if __name__ == "__main__":
    run()