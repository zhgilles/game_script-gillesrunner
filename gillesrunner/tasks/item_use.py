# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_touch, my_swipe, my_exist_and_touch
from gillescommon.position.images import use, select, collect, use_2
from gillescommon.position.points import swipe_point, items, my_items, chest, exit_window


def main():
    my_touch(items, wait_time=1)
    my_touch(my_items, wait_time=1)
    my_touch(chest, wait_time=1)
    while my_exist_and_touch(use):
        my_exist_and_touch(select)
        my_swipe(swipe_point, vector=[0.2461, 0.0294])
        my_exist_and_touch(use_2)
        my_exist_and_touch(collect)
    my_touch(exit_window)





