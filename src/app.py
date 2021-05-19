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
	activity = request.get_json()['activity']
	print('Making the request.')
	return starman_jr.send_message(activity)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
