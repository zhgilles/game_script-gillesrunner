# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from time import sleep

from gillescommon.operation.operation_basic import my_touch, my_exist_and_touch, my_exist
from gillescommon.position.images import select_commander_me, select_troops_2_me, march_2_me, setup_me, queue_add_me, \
    march_3_me, minus_me, search_2_me, touch_2_me, attack_me, troop_list_cross_me, march_4_me, recall_me
from gillescommon.position.points import center_me, plan_me, queue_point_me_2, search_me, whisperers_me, max_level_me, \
    queue_point_me, queue_point_me_3, queue_point_me_4, queue_point_me_5, plan_3_me, plan_4_me, plan_5_me, plan_2_me, \
    multi_select_me


def check_all_troop_return(polling=True):
    polling_time = 5
    max_polling_time = 30
    time = 0
    while polling and time < max_polling_time:
        if not my_exist(troop_list_cross_me):
            return True
        time += polling_time
        sleep(polling_time)
    return not my_exist(troop_list_cross_me)


def _march_troop(point, plan):
    my_touch(point, duration=3)
    my_exist_and_touch(march_3_me, wait_time=3)
    if not my_exist(queue_add_me):
        # 如果没有可以添加的队列 结束
        my_touch(center_me)
    else:
        my_touch(setup_me, wait_time=0.5)
        my_touch(plan)
        if my_exist_and_touch(select_commander_me):
            my_touch(select_troops_2_me)
            my_touch(march_2_me, wait_time=0.5)


def _march_all_troop(points, plans):
    for point, plan in zip(points, plans):
        _march_troop(point, plan)
        sleep(3)


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
    my_touch(attack_me)
    my_touch(multi_select_me)
    my_touch(march_4_me)


def _try_attack_monster(max_retries, monster_lv):
    for _ in range(max_retries):
        try:
            _attack_monster(monster_lv)
            return True
        except:
            pass
    return False


def recall_all_troop():
    my_exist_and_touch(troop_list_cross_me)
    while my_exist_and_touch(recall_me):
        pass


def main():
    success = check_all_troop_return()
    if not success:
        exit()

    plans = [plan_me, plan_2_me, plan_3_me, ]  # plan_4_me, plan_5_me]
    points = [queue_point_me, queue_point_me_2, queue_point_me_3, ]  # queue_point_me_4, queue_point_me_5]
    _march_all_troop(points, plans)

    monster_lv = 28
    max_retries = 3
    success = _try_attack_monster(max_retries, monster_lv)
    if not success:
        recall_all_troop()
