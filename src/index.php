<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;

$message = $_POST['message'];

$client = new Client([
    'base_uri' => 'https://api-inference.huggingface.co/',
    'timeout'  => 2.0,
]);

$response = $client->request('POST', 'models/text-generation/generate', [
    'json' => ['inputs' => $message]
]);

$body = $response->getBody();
$content = json_decode($body->getContents());

echo $content[0]->generated_text;
?>

<!DOCTYPE html>
<html>

<head>
    <title>AI Chat Application</title>
    <style>
        /* Add your CSS here */
        #chatbox {
            width: 300px;
            height: 400px;
            border: 1px solid black;
            overflow: auto;
        }

        #userInput {
            width: 300px;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
</head>

<body>
    <div id="chatbox"></div>
    <input id="userInput" type="text" />
    <button onclick="sendMessage()">Send</button>

    <script>
        function sendMessage() {
            var message = document.getElementById('userInput').value;
            axios.post(window.location.href, {
                    message: message
                })
                .then(function(response) {
                    document.getElementById('chatbox').innerHTML += 'You: ' + message + '<br>';
                    document.getElementById('chatbox').innerHTML += 'AI: ' + response.data.data.generated_text + '<br>';
                    document.getElementById('userInput').value = '';
                })
                .catch(function(error) {
                    console.log(error);
                });
        }
    </script>
</body>

</html>