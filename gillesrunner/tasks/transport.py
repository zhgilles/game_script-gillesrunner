# -*- encoding=utf8 -*-
__author__ = "gillesshi"


import json

from gillescommon.config.rss_config import rss_map_pos
from gillescommon.config.user_config import load_user_config
from gillescommon.operation.operation_basic import my_touch, my_text, my_swipe, my_exist_and_touch
from gillescommon.position.images import exit_window_2
from gillescommon.position.points import magnifier, x_pos, y_pos, confirm, transport, basic_rss, transport_2, go, \
    growth_rss

user_config = load_user_config()


def main(name_target, rss):
    assert name_target in user_config, f"this name {name_target} isn't in config {user_config}"
    pos = json.loads(user_config[name_target][0]['position'])
    my_touch(magnifier)
    my_touch(x_pos)
    my_text(str(pos[0]))
    my_touch(confirm)
    my_touch(y_pos)
    my_text(str(pos[1]))
    my_touch(confirm)
    my_touch(go)
    for rid, times in enumerate(rss.split('#')):
        for i in range(int(times)):
            my_touch(magnifier)
            my_touch(go)
            my_touch(transport)
            if rid//5 == 0:
                my_touch(basic_rss)
            else:
                my_touch(growth_rss)
            my_swipe(rss_map_pos[rid % 5], vector=[0.2461, 0.0294])
            my_touch(transport_2)
      


    
    
    
    
    
    
    
    
    
    
    
    

