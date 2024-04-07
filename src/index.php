<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;

$message = $_POST['message'];

$client = new Client([
    'base_uri' => 'https://huggingface.co/api/models',
    'timeout'  => 2.0,
]);

$response = $client->request('POST', '
/https://huggingface.co/api/models', [
    'json' => ['inputs' => $message]
]);

$body = $response->getBody();
$content = json_decode($body->getContents());

echo $content->generated_text;
?>