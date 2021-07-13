# -*- encoding=utf8 -*-
__author__ = "gillesshi"

import time

from gillescommon.operation.operation_basic import my_exist_and_touch, my_touch
from gillescommon.position.images import map_switch_me, explore_2_me, explore_3_me, dispatch_me, dispatch_2_me, \
    dispatch_3_me, cross_2_me, cross_me, ok_me
from gillescommon.position.points import post_station_me, explore_me, map_switch_2_me


def _explore_me():
    my_touch(post_station_me, wait_time=1)
    my_touch(explore_me, wait_time=1)
    if my_exist_and_touch(explore_2_me, wait_time=2):
        my_exist_and_touch(explore_3_me, wait_time=3)
        for i in [dispatch_me, dispatch_2_me, dispatch_3_me]:
            if my_exist_and_touch(i):
                break
    else:
        my_touch(cross_2_me)


def main():
    for i in range(5):
        _explore_me()
        time.sleep(3)













