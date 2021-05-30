# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_touch, my_exist_and_touch
from gillescommon.position.images import open_10_gifts
from gillescommon.position.points import alliance, gift, ok, clear_expired_gift, exit_window


def main():
    my_touch(alliance)
    my_touch(gift)
    while my_exist_and_touch(open_10_gifts, wait_time=0.5):
        my_touch(ok, wait_time=0.2)
    my_touch(clear_expired_gift)
    my_touch(exit_window)


if __name__ == '__main__':
    main()
