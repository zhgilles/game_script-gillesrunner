# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_exist_and_touch, my_touch
from gillescommon.position.images import map_switch_me, city_switch_me, cross_me, ok_me
from gillescommon.position.points import center_me


def main(scene):
    my_exist_and_touch(cross_me)
    my_exist_and_touch(ok_me)
    if scene == 'map':
        my_touch(center_me)
        my_exist_and_touch(city_switch_me, wait_time=1)
        while my_exist_and_touch(map_switch_me, wait_time=1):
            pass
    elif scene == 'city':
        my_exist_and_touch(map_switch_me, wait_time=1)
        while my_exist_and_touch(city_switch_me, wait_time=1):
            pass

















