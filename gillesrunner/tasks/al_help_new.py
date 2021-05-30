# -*- encoding=utf8 -*-
__author__ = "gillesshi"


from gillescommon.operation.operation_basic import my_exist_and_touch, my_touch
from gillescommon.position.images import al_help, help_all


def main():
    if my_exist_and_touch(al_help):
        my_touch(help_all)


