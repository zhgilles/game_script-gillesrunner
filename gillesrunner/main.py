#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time       : 2021/4/12 11:35
@Author     : gillesshi
@Email      : gillesshi@leyinetwork.com
@File       : main.py
@Software   : PyCharm
@Description: 
"""

import argparse
from gillesrunner.cores.runner import runner


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--task',
        type=str, action='append', required=True, help='任务名称'
    )
    parser.add_argument(
        '-nt', '--name_target',
        type=str, action='store', required=False, help='被送资源的玩家游戏昵称'
    )
    parser.add_argument(
        '-ns', '--name_source',
        type=str, action='store', required=False, help='切换的account名字'
    )
    parser.add_argument(
        '-r', '--rss',
        type=str, action='store', required=False, help='送的资源数量，格式为0#5#5#5#3'
    )
    parser.add_argument(
        '-s', '--scene',
        type=str, action='store', required=False, help='切换场景，可选的范围为：1、城里；2、城里城；3、世界地图'
    )
    parser.add_argument(
        '-ril', '--rss_idx_lst',
        type=str, action='store', required=False, help='使用的资源idx队列，可选范围：0、farm；1、log_yard；2、iron_mine；3、gold_mine'
    )
    args = parser.parse_args()
    print(args)
    return args


def main():
    args = get_args()
    task_list = args.task
    for task in task_list:
        runner(task, args)



if __name__ == '__main__':
    main()
