# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_exist_and_touch, my_touch
from gillescommon.position.images import auto_complete, collect, start
from gillescommon.position.points import quest, town_quest, daily_quest, alliance_quest, vip_quest, exit_window


def main():
    my_touch(quest)
    my_touch(town_quest)
    while my_exist_and_touch(collect):
        pass
    my_touch(daily_quest)
    while my_exist_and_touch(auto_complete):
        pass
    my_touch(alliance_quest)
    while my_exist_and_touch(auto_complete):
        pass
    my_touch(vip_quest)
    my_exist_and_touch(start)
    my_exist_and_touch(collect)
    my_touch(exit_window)

