<?php

require __DIR__.'/vendor/autoload.php';
use GuzzleHttp\Client;
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$app_name = 'your_app_name';
$username = $_ENV['username'];
$password = $_ENV['password'];
$urgency = 'urgent';
$msg_body = 'Guzzle PHP Test';

$client = new Client(['base_uri' => 'http://0.0.0.0:5000/']);
  
$response = $client->request('POST', 'starman_jr/api/v1.0/', ['auth' => [$username, $password],
'json' => ['message' => $msg_body, 'urgency' => $urgency, 'app_name' => $app_name]]);


$msg_body = 'E-Mail test.';
$subject = 'Test';
$app_name = 'your_app_name';
$username = $_ENV['username'];
$password = $_ENV['password'];
$mailto = array('email@provider.com');

$client = new Client(['base_uri' => 'http://0.0.0.0:5000/']);

$response = $client->request('POST', 'starman/api/v1.0/email/', ['auth' => [$username, $password],
'json' => ['message' => $msg_body, 'subject' => $subject, 'app_name' => $app_name, 'mailto' => $mailto]]);
