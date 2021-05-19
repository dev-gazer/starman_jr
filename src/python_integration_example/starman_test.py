import requests
from dotenv import load_dotenv
import os

load_dotenv()

#For Starman
app_name = 'app_test'
username = os.getenv('username')
password = os.getenv('password')


def starman_call (urgency, msg_body):
    requests.post(url='http://0.0.0.0:5000/starman/api/v1.0/',
    json={'message': msg_body, 'urgency': urgency, 'app_name': app_name},
    auth=(username, password))
    return 'Message sent!'


msg_body = f'Request Python'
urgency = 'urgent'
starman_call(urgency, msg_body)
