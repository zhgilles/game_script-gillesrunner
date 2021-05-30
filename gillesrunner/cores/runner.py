#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time       : 2021/4/12 16:56
@Author     : gillesshi
@Email      : gillesshi@leyinetwork.com
@File       : runner
@Software   : PyCharm
@Description: 
"""


from airtest.core.api import auto_setup, ST
from gillesrunner.cores.task import load_tasks
from inspect import signature
import os
import logging
from time import sleep


logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)
TASKS = load_tasks()


def runner(task_name: str, args):
    func = TASKS.get(task_name)
    if not func and task_name.endswith('.py'):
        task_name = os.path.splitext(task_name)[0]
    func = TASKS.get(task_name)
    if not func:
        exit(f"not exist main func in current task: {task_name}")
    ST.FIND_TIMEOUT_TMP = 0.2
    auto_setup(
        __file__
        , logdir=False
        , devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555",
        ]
    )
    fargs = {}
    for req_parm in signature(func).parameters.values():
        req_parm = str(req_parm)
        if not hasattr(args, str(req_parm)):
            exit(f"not exist parm {req_parm} requested for task {task_name}")
        fargs[req_parm] = getattr(args, req_parm)
    func(**fargs)
    logger.info("finish task {task_name}")
    sleep(2)