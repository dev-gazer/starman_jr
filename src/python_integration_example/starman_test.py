import requests
from dotenv import load_dotenv
import os

load_dotenv()

#For Starman
app_name = 'integração propensity ga'
username = os.getenv('username')
password = os.getenv('password')


def starman_call (urgency, msg_body):
    requests.post(url='https://starman-bot-ppw7yxqtsa-uc.a.run.app/starman/api/v1.0/',
    json={'message': msg_body, 'urgency': urgency, 'app_name': app_name},
    auth=(username, password))
    return 'Message sent!'


#msg_body = f'Teste Request Python'
#urgency = 'urgent'
#starman_call(urgency, msg_body)