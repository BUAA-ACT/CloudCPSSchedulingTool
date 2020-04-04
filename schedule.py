#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-03-14
import json
from google.protobuf import text_format

import entity_pb2
import result_pb2
import database
import config


def parse_json_to_entity(jsonObj, entype):

    def parse_App(jsonObj):
        entity = entity_pb2.Entity()
        entity.name = jsonObj.get('Name')
        for item in ['CloudLayer', 'NetworkLayer', 'EndLayer']:
            if item not in jsonObj:
                raise Exception(f'expect {item}, but not found.')
        entity.cloudlayer.MergeFrom(parse_json_to_entity(
                jsonObj.get('CloudLayer'), 'CloudLayer'))
        entity.networklayer.MergeFrom(parse_json_to_entity(
                jsonObj.get('NetworkLayer'), 'NetworkLayer'))
        entity.endlayer.MergeFrom(parse_json_to_entity(
                jsonObj.get('EndLayer'), 'EndLayer'))
        # do not need links
        return entity

    def parse_CloudLayer(jsonObj):
        entity = entity_pb2.CloudLayer()
        for item in ['Datacenters']:
            if item not in jsonObj:
                raise Exception(f'expect {item}, but not found.')
        for datacenter in jsonObj.get('Datacenters'):
            entity.datacenters.append(parse_json_to_entity(
                datacenter, 'Datacenters'))
        return entity

    def parse_Datacenters(jsonObj):
        entity = entity_pb2.Datacenter()
        #  entity.id = jsonObj.get('DatacenterID')
        entity.location = jsonObj.get('Location')
        #  entity.name = jsonObj.get('Name')
        for item in ['CloudNodes']:
            if item not in jsonObj:
                raise Exception(f'expect {item}, but not found.')
        for cloudnode in jsonObj.get('CloudNodes'):
            entity.cloudnodes.append(parse_json_to_entity(
                cloudnode, 'CloudNodes'))
        return entity

    def parse_CloudNodes(jsonObj):
        entity = entity_pb2.CloudNode()
        entity.id = jsonObj.get('CloudNodeID')
        #  entity.name = jsonObj.get('Name')
        entity.location = jsonObj.get('Location')
        for item in ['Containers']:
            if item not in jsonObj:
                raise Exceptio(f'expect {item}, but not found.')
        for container in jsonObj.get('Containers'):
            entity.containers.append(parse_json_to_entity(
                container, 'Containers'))
        return entity

    def parse_Containers(jsonObj):
        entity = entity_pb2.Container()
        entity.id = jsonObj.get('ContainerID')
        #  entity.name = jsonObj.get('Name')
        entity.cpu = int(jsonObj.get('CpuNumber'))
        entity.memory = int(jsonObj.get('Memory'))
        entity.store = int(jsonObj.get('Store'))
        return entity

    def parse_NetworkLayer(jsonObj):
        entity = entity_pb2.NetworkLayer()
        
        # 目前没有 networklayer 资源
        return entity
        
        for item in ['NetNodes', 'EdgeServers']:
            if item not in jsonObj:
                if item == 'EdgeServers':
                    continue
                raise Exception(f'expect {item}, but not found.')
            for subJsonObj in jsonObj.get(item):
                if item == 'EdgeServers':
                    entity.edgeservers.append(parse_json_to_entity(
                        subJsonObj, item))
                elif item == 'NetNodes':
                    entity.netnodes.append(parse_json_to_entity(
                        subJsonObj, item))
        return entity

    def parse_NetNodes(jsonObj):
        entity = entity_pb2.NetNode()
        entity.id = jsonObj.get('NetNodeID')
        #  entity.name = jsonObj.get('Name')
        entity.location = jsonObj.get('Location')
        # Containers can also in EdgeServers
        for item in ['Containers']:
            if item in jsonObj:
                entity.containers.append(parse_json_to_entity(
                    jsonObj.get(item), item))
        return entity

    def parse_EdgeServers(jsonObj):
        entity = entity_pb2.EdgeServer()
        entity.id = jsonObj.get('EdgeServerID')
        #  entity.name = jsonObj.get('Name')
        entity.location = jsonObj.get('Location')
        # Containers can also in EdgeServers
        for item in ['Containers']:
            if item in jsonObj:
                entity.containers.append(parse_json_to_entity(
                    jsonObj.get(item), item))
        return entity

    def parse_EndLayer(jsonObj):
        entity = entity_pb2.EndLayer()
        items = ['Devices', 'Workers', 'Applications', 'Rooms']
        empty = True
        general_room = None
        for item in items:
            if item not in jsonObj:
                continue
            empty = False
            for subJsonObj in jsonObj.get(item):
                if item == 'Rooms':
                    entity.rooms.append(parse_json_to_entity(
                        subJsonObj, item))
                else:
                    if general_room is None:
                        general_room = entity_pb2.Room()
                        general_room.name = 'GeneralRoom'
                        general_room.location = 'Logical'
                    if item == 'Devices':
                        general_room.devices.append(parse_json_to_entity(
                            subJsonObj, item))
                    elif item == 'Workers':
                        general_room.workers.append(parse_json_to_entity(
                            subJsonObj, item))
                    elif item == 'Applications':
                        general_room.applications.append(parse_json_to_entity(
                            subJsonObj, item))
        if general_room is not None:
            entity.rooms.append(general_room)
        if empty:
            raise Exception(f'expect {items}, but not found anything.')
        return entity

    def parse_Rooms(jsonObj):
        entity = entity_pb2.Room()
        #  entity.name = jsonObj.get('Name')
        entity.location = jsonObj.get('Location')
        items = ['Devices', 'Workers', 'Applications']
        empty = True
        for item in items:
            if item not in jsonObj:
                continue
            empty = False
            for subJsonObj in jsonObj.get(item):
                if item == 'Devices':
                    entity.devices.append(parse_json_to_entity(
                        subJsonObj, item))
                elif item == 'Workers':
                    entity.workers.append(parse_json_to_entity(
                        subJsonObj, item))
                elif item == 'Applications':
                    entity.applications.append(parse_json_to_entity(
                        subJsonObj, item))
        if empty:
            raise Exception(f'expect {items}, but not found anything.')
        return entity

    def parse_Devices(jsonObj):
        entity = entity_pb2.Device()
        entity.name = jsonObj.get('Name')
        entity.id = jsonObj.get('DeviceID')
        return entity

    def parse_Workers(jsonObj):
        entity = entity_pb2.Worker()
        entity.name = jsonObj.get('Name')
        entity.id = jsonObj.get('WorkerID')
        return entity

    def parse_Applications(jsonObj):
        entity = entity_pb2.Application()
        entity.name = jsonObj.get('Name')
        entity.id = jsonObj.get('ApplicationID')
        return entity

    parse = {
        'App': parse_App,
        'CloudLayer': parse_CloudLayer,
        'Datacenters': parse_Datacenters,
        'CloudNodes': parse_CloudNodes,
        'Containers': parse_Containers,
        'NetworkLayer': parse_NetworkLayer,
        'NetNodes': parse_NetNodes,
        'EdgeServers': parse_EdgeServers,
        'EndLayer': parse_EndLayer,
        'Rooms': parse_Rooms,
        'Devices': parse_Devices,
        'Workers': parse_Workers,
        'Applications': parse_Applications,
    }
    return parse[entype](jsonObj)


def receive(jsonObj):    
    return parse_json_to_entity(jsonObj, 'App')


def queryResources(database):
    '''
    with open('./resource.prototxt') as f:
        resources = entity_pb2.Entity()
        text_format.Parse(f.read(), resources)
    return resources
    '''
    entity = entity_pb2.Entity()
    entity.name = 'resources'
    
    cloudlayer = entity_pb2.CloudLayer()
    datacenters_dict = {}
    servers = database.queryNewestItems('serverinfo',
                                        timelabel='time')
    for server in servers:
        [sid, name, ip, cpuUnusage, diskIORead, diskIOWrite,
                diskUsed, memoryUsed, networkUploadRate,
                networkDownloadRate, time, cpuNum, dataCenter,
                memoryAvailable, diskAvailable] = server
        cpuUsage = 1 - cpuUnusage
        print(f"id: %d, " % sid + \
              f"name: {name}, " + \
              f"cpuNum: {cpuNum * (1 - cpuUsage)}, " + \
              f"memoryAvailable: {memoryAvailable}, " + \
              f"diskAvailable: {diskAvailable}")
        cloudnode = entity_pb2.CloudNode()
        cloudnode.id = '%d' % sid
        cloudnode.location = name
        cloudnode.cpu = cpuNum * (1 - cpuUsage)
        cloudnode.memory = memoryAvailable
        cloudnode.store = diskAvailable
        if dataCenter not in datacenters_dict:
            datacenters_dict[dataCenter] = entity_pb2.Datacenter()
            datacenters_dict[dataCenter].location = dataCenter
        datacenters_dict[dataCenter].cloudnodes.append(cloudnode)
    for location, datacenter in datacenters_dict.items():
        cloudlayer.datacenters.append(datacenter)
    entity.cloudlayer.MergeFrom(cloudlayer)

    '''
    containers = database.queryNewestItems("dockerinfo",
                                           timelabel='time')
    for container in containers:
        [sid, name, dockerid, cpuUsage, memUsage,
                diskIORead, diskIOWrite, memoryUsed,
                networkIORead, networkIOWrite, time,
                cpuMem, memoryAvailable, diskAvailable] = container
        print(f"id: {dockerid}, " + \
              f"serverid: %d, " % sid + \
              f"name: {name}, " + \
              f"cpuNum: {cpuNum * (1 - cpuUsage)}, " + \
              f"memoryAvailable: {memoryAvailable}, " + \
              f"diskAvailable: {diskAvailable}")
    '''

    networklayer = entity_pb2.NetworkLayer()
    entity.networklayer.MergeFrom(networklayer) # 暂时没有networklayer

    endlayer = entity_pb2.EndLayer()
    rooms_dict = {}
    devices = database.queryItems('deviceinfo',
                                  'inroom="True"')
    for device in devices:
        [did, localip, inroom, token, dtype, model,
                name, data, location, timestamp] = device
        print(f"id: {did}, " + \
              f"inroom: {inroom}, " + \
              f"name: {name}, " + \
              f"location: {location}")
        if inroom != "True":
            continue
        device = entity_pb2.Device()
        device.name = name
        device.id = did
        if location not in rooms_dict:
            rooms_dict[location] = entity_pb2.Room()
            rooms_dict[location].location = location
        rooms_dict[location].devices.append(device)
    for location, room in rooms_dict.items():
        endlayer.rooms.append(room)
    entity.endlayer.MergeFrom(endlayer)

    return entity


def dfs(demand_idx, demand, resources, used, match, dfs_type, res):
    for resource_idx, resource in enumerate(resources):
        if bipartite_graph_match(demand, resource, dfs_type, res) \
                and not used[resource_idx]:
            used[resource_idx] = True
            if match[resource_idx] == -1 or \
                    dfs(match[resource_idx], demand, resources,
                            used, match, dfs_type, res):
                match[resource_idx] = demand_idx
                return True
    return False


def bipartite_graph_match(demands, resources, match_type, res):
    if match_type == 'cloudlayer':
        dn = len(demands.datacenters)
        an = len(resources.datacenters)
        match_num = 0
        match = [-1 for x in range(an)]
        for demand_idx, demand in enumerate(demands.datacenters):
            used = [0 for x in range(an)]
            if dfs(demand_idx, demand, resources.datacenters, 
                    used, match, 'datacenters', res):
                match_num += 1
        if match_num != dn:
            return False
        return True
    elif match_type == 'datacenters':
        dn = len(demands.cloudnodes)
        an = len(resources.cloudnodes)
        match_num = 0
        match = [-1 for x in range(an)]
        for demand_idx, demand in enumerate(demands.cloudnodes):
            used = [0 for x in range(an)]
            if dfs(demand_idx, demand, resources.cloudnodes, 
                    used, match, 'cloudnodes', res):
                match_num += 1
        if match_num != dn:
            return False
        res.update({demands.cloudnodes[di].id:resources.cloudnodes[ai].id
                for ai, di in enumerate(match)})
        container_match = {}
        for ai, di in enumerate(match):
            for container in demands.cloudnodes[di].containers:
                container_match[container.id] = resources.cloudnodes[ai].id
        res.update(container_match)
        return True
    elif match_type == 'networklayer':
        # netnodes part
        netnodes_dn = len(demands.netnodes)
        netnodes_an = len(resources.netnodes)
        netnodes_match_num = 0
        netnodes_match = [-1 for x in range(netnodes_an)]
        for demand_idx, demand in enumerate(demands.netnodes):
            netnodes_used = [0 for x in range(netnodes_an)]
            if dfs(demand_idx, demand, resources.netnodes, 
                    netnodes_used, netnodes_match,
                    'netnodes', res):
                netnodes_match_num += 1
        if netnodes_match_num != netnodes_dn:
            return False
        # edgeservers part
        edgeservers_dn = len(demands.edgeservers)
        edgeservers_an = len(resources.edgeservers)
        edgeservers_match_num = 0
        edgeservers_match = [-1 for x in range(edgeservers_an)]
        for demand_idx, demand in enumerate(demands.edgeservers):
            edgeservers_used = [0 for x in range(edgeservers_an)]
            if dfs(demand_idx, demand, resources.edgeservers, 
                    edgeservers_used, edgeservers_match,
                    'edgeservers', res):
                edgeservers_match_num += 1
        if edgeservers_match_num != edgeservers_dn:
            return False
        res.update({demands.netnodes[di].id:resources.netnodes[ai].id 
                    for ai, di in enumerate(netnodes_match)})
        res.update({demands.edgeservers[di].id:resources.edgeservers[ai].id
                    for ai, di in enumerate(edgeservers_match)})
        container_match = {}
        for ai, di in enumerate(netnodes_match):
            for container in demands.netnodes[di].containers:
                container_match[container.id] = resources.netnodes[ai].id
        for ai, di in enumerate(edgeservers_match):
            for container in demands.edgeservers[di].containers:
                container_match[container.id] = resources.edgeservers[ai].id
        res.update(container_match)
        return True
    elif match_type == 'endlayer':
        dn = len(demands.rooms)
        an = len(resources.rooms)
        match_num = 0
        match = [-1 for x in range(an)]
        for demand_idx, demand in enumerate(demands.rooms):
            used = [0 for x in range(an)]
            if dfs(demand_idx, demand, resources.rooms,
                    used, match, 'rooms', res):
                match_num += 1
        if match_num != dn:
            return False
        return True
    elif match_type == 'rooms':
        # devices part
        devices_dn = len(demands.devices)
        devices_an = len(resources.devices)
        devices_match_num = 0
        devices_match = [-1 for x in range(devices_an)]
        for demand_idx, demand in enumerate(demands.devices):
            devices_used = [0 for x in range(devices_an)]
            if dfs(demand_idx, demand, resources.devices, 
                    devices_used, devices_match,
                    'devices', res):
                devices_match_num += 1
        if devices_match_num != devices_dn:
            return False
        # workers part
        workers_dn = len(demands.workers)
        workers_an = len(resources.workers)
        workers_match_num = 0
        workers_match = [-1 for x in range(workers_an)]
        for demand_idx, demand in enumerate(demands.workers):
            workers_used = [0 for x in range(workers_an)]
            if dfs(demand_idx, demand, resources.workers, 
                    workers_used, workers_match,
                    'workers', res):
                workers_match_num += 1
        if workers_match_num != workers_dn:
            return False
        # applications part
        applications_dn = len(demands.applications)
        applications_an = len(resources.applications)
        applications_match_num = 0
        applications_match = [-1 for x in range(applications_an)]
        for demand_idx, demand in enumerate(demands.applications):
            applications_used = [0 for x in range(applications_an)]
            if dfs(demand_idx, demand, resources.applications, 
                    applications_used, applications_match,
                    'applications', res):
                applications_match_num += 1
        if applications_match_num != applications_dn:
            return False
        res.update({demands.devices[di].id:resources.devices[ai].id 
                    for ai, di in enumerate(devices_match)})
        res.update({demands.workers[di].id:resources.workers[ai].id
                    for ai, di in enumerate(workers_match)})
        res.update({demands.applications[ai].id:resources.applications[ai].id
                    for ai, di in enumerate(applications_match)})
        return True
    elif match_type in ['cloudnodes', 'netnodes', 'edgeservers']:
        demand_cpu = 0
        demand_mem = 0
        demand_sto = 0
        for container in demands.containers:
            demand_cpu += container.cpu
            demand_mem += container.memory
            demand_sto += container.store
        if demand_cpu > resources.cpu:
            return False
        if demand_mem > resources.memory:
            return False
        if demand_sto > resources.store:
            return False
        return True
    elif match_type in ['devices', 'workers', 'applications']:
        if demands.name != resources.name:
            return False
        return True
    else:
        raise Exception(f'error match type: {match_type}')


def schedule(demands, resources):
    res = {}
    cloudlayer = bipartite_graph_match(
            demands.cloudlayer, resources.cloudlayer,
            'cloudlayer', res)
    if not cloudlayer:
        print('cloudlayer can not schedule.')
        return None
    networklayer = bipartite_graph_match(
            demands.networklayer, resources.networklayer,
            'networklayer', res)
    if not networklayer:
        print('networklayer can not schedule.')
        return None
    endlayer = bipartite_graph_match(
            demands.endlayer, resources.endlayer,
            'endlayer', res)
    if not endlayer:
        print('endlayer can not schedule.')
        return None
    
    result = result_pb2.Result()
    result.appname = demands.name
    for did, sid in res.items():
        mth = result_pb2.Match()
        mth.demandid = did
        mth.resourceid = sid
        result.matchs.append(mth)
    return result


def writeToTable(database, table, result):
    for match in result.matchs:
        params = {'appName': result.appname,
                  'demandid': match.demandid,
                  'resourceid': match.resourceid}
        database.insert(table, params)


def print_proto(proto):
    text = text_format.MessageToString(proto, as_utf8=True)
    print(text)


def save_proto(proto, filename):
    with open(filename, 'w') as f:
        f.write(text_format.MessageToString(proto, as_utf8=True))


if __name__ == '__main__':
    database_manager = database.DatabaseManager(
            config.DATABASE.remote_ip, config.DATABASE.remote_usr,
            config.DATABASE.remote_pwd, config.DATABASE.database_usr,
            config.DATABASE.database_pwd, config.DATABASE.database_name)
    with open('./demand.hrm') as f:
        jsonObj = json.loads(f.read())
        demands = receive(jsonObj)
    resources = queryResources(database_manager)
    save_proto(demands, 'demands.prototxt')
    save_proto(resources, 'resources.prototxt')
    print_proto(demands)
    print_proto(resources)
    result = schedule(demands, resources)
    print_proto(result)
    writeToTable(database_manager, 'matchtable', result)
    database_manager.__del__()
