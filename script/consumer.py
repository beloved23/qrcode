from kafka import KafkaConsumer
from json import loads
import os, sys
from datetime import date, datetime
import logging
import json, ast
import django
import datetime
from django.utils.timezone import make_aware

LOG_FILE = '/opt/software/var/scanner/consumer-%s.log' % date.today()
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(message)s|[%(asctime)s]')
APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)
sys.path.append(BASE_DIR)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scannerr.settings")
django.setup()

from mobile.models import AppRegistration
from dateutil import parser



consumer = KafkaConsumer(
    'selfcareonboarding',
     bootstrap_servers=['172.24.6.64:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


def process_kafka():
    for message in consumer:
        try:
            message = message.value
            data = {}
            logging.info('{}'.format(message))
            for k in message.keys():
                data[k] = message[k]
            data['lastLoginDate'] = make_aware(datetime.datetime.fromtimestamp(float(message['lastLoginDate'])/1000).strftime('%Y-%m-%d %H:%M:%S'))
            data['createdDate'] = make_aware(datetime.datetime.fromtimestamp(float(message['lastLoginDate'])/1000).strftime('%Y-%m-%d %H:%M:%S'))
            action = AppRegistration(**data)
            action.save()
        except Exception,ex:
            logging.info("An error occurred %s" % str(ex))


process_kafka()



