#!/bin/python3
import os, sys
from dotenv import load_dotenv
import datetime
import pymysql
import requests

load_dotenv()

def get_telegram(activity):
    try:
        mysql_password = os.getenv('mysqlpass')
        my_sql_user = os.getenv('user')

        #####################################################
        #host and con for usage in localhost (whether or not containerized).
        host = os.getenv('host')
        con = pymysql.connect(host=host, user=my_sql_user, passwd=mysql_password, db='starman_jr', cursorclass=pymysql.cursors.DictCursor)
        #####################################################

        #####################################################
        #unix_socket e con used on production environment (Google Cloud SQL Instance).
        #unix_socket = os.getenv('unix_socket')
        #con = pymysql.connect(unix_socket=unix_socket, user=my_sql_user, passwd=mysql_password, db='starman', cursorclass=pymysql.cursors.DictCursor)
        #####################################################
        
        cursor = con.cursor()
        cursor.execute(f"SELECT person_id, person_name, activity_name FROM `activities` WHERE activity_id = '{activity}';")

        rows = cursor.fetchall()
        names = []
        telegrams = []
        activities = []
        for row in rows:
            names.append(row['person_name'])
            telegrams.append(row['person_id'])
            activities.append(row['activity_name'])
        con.commit()
        con.close()
    except:
        print(f'Activity {activity} not found on Starman database.')
        sys.exit(f'Activity {activity} not found on Starman database.')
    return names, telegrams, activities

def send_telegram(message, telegram):
    auth_token = os.getenv('TELEGRAM_TOKEN')
    send_text = f"https://api.telegram.org/bot{auth_token}/sendMessage?chat_id={telegram}&parse_mode=Markdown&text={message}"
    response = requests.get(send_text)
    return 'Message sent via Telegram!'

def send_message(activity):
    names, telegrams, activities = get_telegram(activity)
    for name in names:
        message = f'{name}, how you doin?\n{activities[names.index(name)]}'
        telegram = telegrams[names.index(name)]
        send_telegram(message, telegram)
    return