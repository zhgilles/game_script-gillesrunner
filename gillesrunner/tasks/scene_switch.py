# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_touch, my_exist, my_swipe
from gillescommon.position.points import center, world_map
from gillescommon.position.images import town_tag


def main(scene):  # town world inner_town
    my_swipe(center, vector=(1, 1))
    my_swipe(center, vector=(1, 1))
    town = my_exist(town_tag)
    if (town and scene == 'world') or (not town and scene == 'town'):
        my_touch(world_map, wait_time=5)
