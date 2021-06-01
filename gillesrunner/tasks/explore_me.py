# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_exist_and_touch, my_touch
from gillescommon.position.images import map_switch_me, explore_2_me, explore_3_me, dispatch_me, dispatch_2_me, \
    dispatch_3_me
from gillescommon.position.points import post_station_me, explore_me


def main():
    while my_exist_and_touch(map_switch_me, wait_time=1):
        pass
    my_touch(post_station_me, wait_time=0.5)
    my_touch(explore_me, wait_time=0.5)
    my_exist_and_touch(explore_2_me, wait_time=1)
    my_exist_and_touch(explore_3_me, wait_time=0.5)
    for i in [dispatch_me, dispatch_2_me, dispatch_3_me]:
        if my_exist_and_touch(i, wait_time=0.5):
            break













