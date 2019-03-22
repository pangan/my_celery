# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>
Python Version: 3.7
"""
from my_app.fetch_celery.tasks import add
from celery.result import AsyncResult

from time import sleep

# result = long_running_task.s().delay()

task = add.apply_async((0,), task_id='1234')

task_id = task.task_id


while True:
    res = AsyncResult('1234')
    while not res.ready():
        pass

    my_result = None
    try:
        my_result = res.get(2)
    except Exception:
        print('Time out!')

    print(my_result)
    sleep(20)

