from flask import Flask, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os
import datetime
import starman_jr

load_dotenv()

auth = HTTPBasicAuth()

app = Flask(__name__)

users = {
    os.getenv('username'): generate_password_hash(os.getenv('password'))
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/starman_jr/api/v1.0/', methods=['POST'])
@auth.login_required
def send_message():
	message = request.get_json()['message']
	urgency = request.get_json()['urgency']
	app_name = request.get_json()['app_name']
	print('Making the request.')
	return starman_jr.send_message(message, urgency, app_name)

@app.route('/starman_jr/api/v1.0/email/', methods=['POST'])
@auth.login_required
def send_email():
	message = request.get_json()['message']
	app_name = request.get_json()['app_name']
	subject = request.get_json()['subject']
	mailto = request.get_json()['mailto']
	attach_list = request.get_json()['attach_list']
	print('Sending e-mail')
	return starman_jr.send_email(message, app_name, subject, mailto, attach_list)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)