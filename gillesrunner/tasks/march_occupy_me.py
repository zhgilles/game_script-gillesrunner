# -*- encoding=utf8 -*-
__author__ = "gillesshi"

import time

from gillescommon.operation.operation_basic import my_exist_and_touch, my_touch, my_exist
from gillescommon.position.images import cross_me, ok_me, search_2_me, minus_me, touch_2_me, gather_me, setup_me, \
    march_me, queue_add_me
from gillescommon.position.points import search_me, iron_mine_me, \
    log_yard_me, farm_me, max_level_me, center_me, gold_mine_me


def _chose_resource(resource):
    my_touch(search_me, wait_time=0.5)
    my_touch(resource)
    my_touch(max_level_me)
    while True:
        my_touch(search_2_me, wait_time=1.5)
        if my_exist_and_touch(touch_2_me):
            break
        my_touch(minus_me)
    if not my_exist_and_touch(gather_me):
        return False
    return True


def _march_occupy(resource):
    my_exist_and_touch(cross_me)
    my_exist_and_touch(ok_me)
    my_touch(center_me)
    success = _chose_resource(resource)
    if success:
        if not my_exist(queue_add_me):
            my_touch(center_me)
        else:
            my_touch(setup_me, wait_time=0.5)
            my_touch(march_me)


def main():
    for resource in [iron_mine_me, log_yard_me, farm_me, gold_mine_me, iron_mine_me, log_yard_me, farm_me, gold_mine_me]:
        _march_occupy(resource)
        time.sleep(3)













