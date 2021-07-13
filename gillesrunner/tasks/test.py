#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time       : 2021/4/13 21:52
@Author     : gillesshi
@Email      : gillesshi@leyinetwork.com
@File       : test.py
@Software   : PyCharm
@Description: 
"""
from gillescommon.position.images import open_10_gifts, cross_2, bull_gang_challenge, event_calendar, cross, cross_me, \
    march_3_me, troop_list_cross_me, minus_me, search_2_me, touch_2_me, attack_me, march_4_me
from gillescommon.position.points import ok, cross_3, plan_me, plan_2_me, whisperers_me, search_me, max_level_me, \
    multi_select_me
from gillescommon.operation.operation_basic import my_touch, my_exist_and_touch, my_exist


def main():
    def _attack_monster(monster_lv):
        max_monster_lv = 28
        my_touch(search_me, wait_time=0.5)
        my_touch(whisperers_me)
        my_touch(max_level_me)
        for _ in range(max_monster_lv - monster_lv):
            my_touch(minus_me)
        while True:
            my_touch(search_2_me, wait_time=2)
            if my_exist_and_touch(touch_2_me):
                break
            my_touch(minus_me)
        my_touch(multi_select_me)
        my_exist_and_touch(march_4_me)

    monster_lv = 28
    _attack_monster(monster_lv)

    # my_touch(touch_2_me, wait_time=1)
