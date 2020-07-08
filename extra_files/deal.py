#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-04-04
from scheduletool import schedule
from scheduletool import database
import json


with open('demand.hrm') as f:
    data = json.loads(f.read())

demands = schedule.receive(data)

database_manager = database.DatabaseManager(
        '39.104.154.79', 'wangch', '20191104wc',
        'root', '20191104', 'node_infos')

resources = schedule.queryResources(database_manager)
result = schedule.schedule(demands, resources, rtype='json')
print(result)
