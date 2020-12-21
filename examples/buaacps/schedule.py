#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-03-14
import json
import config
from scheduletool.buaacps import database, schedule

if __name__ == '__main__':
    with open('./demand.hrm') as f:
        jsonObj = json.loads(f.read())
        demands = schedule.receive(jsonObj)
    database_manager = database.DatabaseManager(
            config.DATABASE['remote_ip'], config.DATABASE['remote_usr'],
            config.DATABASE['remote_pwd'], config.DATABASE['database_usr'],
            config.DATABASE['database_pwd'], config.DATABASE['database_name'])
    resources = schedule.queryResources(database_manager)
    schedule.save_proto(demands, 'demands.prototxt')
    schedule.save_proto(resources, 'resources.prototxt')
    schedule.print_proto(demands)
    schedule.print_proto(resources)
    result = schedule.schedule(demands, resources, rtype='json')
    #  schedule.writeToTable(database_manager, 'matchtable', result)
    print(result)
