# -*- encoding=utf8 -*-
__author__ = "gillesshi"


from gillescommon.operation.operation_basic import my_touch
from gillescommon.position.points import mail, mail_2, instant_check, o3, o4, o5, event_mail, o6, exit_window


def main():
    my_touch(mail)

    my_touch(mail_2)
    my_touch(instant_check)
    my_touch(o3)
    my_touch(o4)
    my_touch(o5)
        
    my_touch(event_mail)
    my_touch(instant_check)
    my_touch(o6)

    my_touch(exit_window)
