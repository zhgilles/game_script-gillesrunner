# -*- encoding=utf8 -*-
__author__ = "gillesshi"

from gillescommon.operation.operation_basic import my_touch, my_text, my_keyevent, my_exist, my_exist_and_touch
from gillescommon.config.user_config import load_user_config
from gillescommon.position.points import more, leyi_account_email, confirm, password, cross_3
from gillescommon.position.images import account, switch_account, yes, login, cross_2, cross, bull_gang_challenge, \
    event_calendar


user_config = load_user_config()


def main(name_source):
    assert name_source in user_config, f"this name {name_source} isn't in config {user_config}"
    my_touch(more)
    my_touch(account)
    my_touch(switch_account)
    my_touch(yes, wait_time=2)

    my_touch(leyi_account_email)
    my_keyevent("KEYCODE_DEL")
    my_text(user_config[name_source][0]['account'], wait_time=1)
    my_touch(confirm)

    my_touch(password)
    my_keyevent("KEYCODE_DEL")
    my_text(user_config[name_source][0]['password'], wait_time=1)
    my_touch(confirm, wait_time=1)

    my_touch(login, wait_time=30)

    if my_exist(bull_gang_challenge):
        my_touch(cross_3, wait_time=0.5)

    if my_exist(event_calendar):
        my_touch(cross_2, wait_time=0.5)

    my_exist_and_touch(cross)
