# LocalAI Chat

LocalAI Chat is a simple web application that allows users to interact with a locally hosted AI model. The application is built using Flask for the backend and streams the AI's responses to the frontend dynamically using Server-Sent Events (SSE).

## Features

- Ask questions and receive AI-generated responses in real-time.
- Dynamically updates the UI with responses as they are generated.
- Simple and clean user interface.

## Screenshots

![Screenshot](/static/screenshot.png)

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.7 or higher
- Flask
- requests

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrohith29/localAI.git
   cd localAI

2. Create a virtual environment and activate it

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

### Running the Application

1. Start the flask server
    ```bash
    python app.py

2. Open your browser and go to `http://127.0.0.1:5000`
   
3. Enter your question in the textarea and submit the form to see the AI's response streamed in real-time.

### Project Structure

    localai-chat/
    │
    ├── static/
    │   └── styles.css
    │
    ├── templates/
    │   └── index.html
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

### License

This project is licensed under the MIT License - see the <a href='https://github.com/mrohith29/localAI/blob/main/LICENSE'>LICENSE</a> file for details.

### Acknowledgments

- Thanks to the open-source community for providing tools and resources to make this project possible.

    ```css
    Feel free to adjust the content according to your project's specific details and preferences.
