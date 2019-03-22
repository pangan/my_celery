# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>
Python Version: 3.7
"""

import random
from my_app.fetch_celery.worker import app


@app.task(bind=True, name='long_running_task')
def long_running_task(self):
    n = 100000
    total = 0
    for i in range(0, n):
        total += random.randint(1, 1000)
    return total / n

@app.task
def add(a):
    task = add.apply_async((a + 1,), task_id='1234', countdown=10)
    return a + 1
