# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>
Python Version: 3.7
"""

import os
from celery import Celery

from my_app import settings

# os.environ['CELERY_BACKEND_FOLDER'] = '/Users/amir/dev/my_test/results'
# os.environ['CELERY_BROKER_FOLDER'] = '/Users/amir/dev/my_test/broker2'

broker_url = os.getenv('CELERY_BROKER_URL', 'filesystem://')
broker_dir = os.getenv('CELERY_BROKER_FOLDER', settings.CELERY_BROKER_FOLDER)

backend_dir = os.getenv('CELERY_BACKEND_FOLDER', settings.CELERY_BACKEND_FOLDER)

for f in ['out', 'processed']:
    if not os.path.exists(os.path.join(broker_dir, f)):
        os.makedirs(os.path.join(broker_dir, f))

backend_abs = os.path.abspath(backend_dir)
if not os.path.exists(backend_abs):
    os.makedirs(backend_abs)


app = Celery(__name__)
app.conf.update({
    'broker_url': broker_url,
    'broker_transport_options': {
        'data_folder_in': os.path.join(broker_dir, 'out'),
        'data_folder_out': os.path.join(broker_dir, 'out'),
        'data_folder_processed': os.path.join(broker_dir, 'processed')
    },
    'imports': ('my_app.fetch_celery.tasks',),
    'result_persistent': False,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'result_backend': 'file://{}'.format(backend_abs),
    'accept_content': ['json']})
