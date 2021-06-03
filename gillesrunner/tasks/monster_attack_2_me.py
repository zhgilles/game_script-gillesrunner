# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from time import sleep

from gillescommon.operation.operation_basic import my_touch, my_exist_and_touch, my_exist
from gillescommon.position.images import search_2_me, touch_2_me, attack_me, select_commander_me, cross_me, \
    select_troops_me, march_me, setup_me, queue_add_me, minus_me, ok_me
from gillescommon.position.points import search_me, whisperers_me, plan_1_me, plan_2_me, center_me, plan_3_me, \
    whisperers_max_level_me, plan_4_me

plan_idx = 0
monster_level_offset = 0


def _chose_monster(i):
    global monster_level_offset
    my_touch(search_me, wait_time=0.5)
    my_touch(whisperers_me)
    if i == 0:
        my_touch(whisperers_max_level_me)
    elif monster_level_offset > 2:
        my_touch(minus_me)
    while True:
        my_touch(search_2_me, wait_time=1.5)
        if my_exist_and_touch(touch_2_me):
            break
        my_touch(minus_me)
        monster_level_offset += 1
    if not my_exist_and_touch(attack_me):
        return False
    return True


def _chose_queue(plan_lst):
    global plan_idx
    if not my_exist(queue_add_me):
        my_touch(center_me)
    else:
        my_touch(setup_me)
        j = 0
        while j < len(plan_lst):
            my_touch(plan_lst[plan_idx])
            if my_exist_and_touch(select_commander_me):
                my_touch(select_troops_me)
                my_touch(march_me, wait_time=1)
                break
            plan_idx = (plan_idx+1) % len(plan_lst)
            j += 1
        if j == len(plan_lst):
            my_touch(cross_me, wait_time=1)


def _attack_monster(i, plan_lst):
    my_exist_and_touch(cross_me)
    my_exist_and_touch(ok_me)
    my_touch(center_me)
    success = _chose_monster(i)
    if success:
        _chose_queue(plan_lst)


def main():
    plan_lst = [plan_1_me, plan_2_me, plan_3_me, plan_4_me]
    for i in range(4):
        _attack_monster(i, plan_lst)
        sleep(1)














