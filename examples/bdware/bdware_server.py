#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-19
from scheduletool.bdware.server import ScheduleServer
import logging

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M',
        level=logging.INFO)

if __name__ == "__main__":
    server = ScheduleServer()
    server.start(2, 18067)
