<?php

require __DIR__.'/vendor/autoload.php';
use GuzzleHttp\Client;
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();
/*
$app_name = 'identified sale';
$username = $_ENV['username'];
$password = $_ENV['password'];
$urgency = 'urgent';
$msg_body = 'Teste Guzzle PHP';

$client = new Client(['base_uri' => 'https://starman-bot-ppw7yxqtsa-uc.a.run.app/']);
  
$response = $client->request('POST', 'starman/api/v1.0/', ['auth' => [$username, $password],
'json' => ['message' => $msg_body, 'urgency' => $urgency, 'app_name' => $app_name]]);
*/

$msg_body = 'Teste de email via request em php.';
$subject = 'Teste';
$app_name = 'identified sale';
$username = $_ENV['username'];
$password = $_ENV['password'];
$mailto = array('martuscellifaria@gmail.com', 'martuscellifaria@usp.br', 'menttheband@gmail.com');

$client = new Client(['base_uri' => 'http://0.0.0.0:5000/']);

$response = $client->request('POST', 'starman/api/v1.0/email/', ['auth' => [$username, $password],
'json' => ['message' => $msg_body, 'subject' => $subject, 'app_name' => $app_name, 'mailto' => $mailto]]);