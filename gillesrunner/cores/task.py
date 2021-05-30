#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time       : 2021/4/12 16:56
@Author     : gillesshi
@Email      : gillesshi@leyinetwork.com
@File       : tasks
@Software   : PyCharm
@Description: 
"""

from gillesrunner import tasks
from pkgutil import walk_packages
from typing import Dict, Callable, Iterable, Any, List
from importlib import import_module


def load_tasks() -> Dict[str, Callable]:
    res = {}
    for m in walk_packages(tasks.__path__, tasks.__name__ + '.'):
        task = import_module(m.name)
        if hasattr(task, 'main') and isinstance(
                task.main, Callable):
            name = m.name.split('.')[-1]
            func = task.main
            res[name] = func
    return res
