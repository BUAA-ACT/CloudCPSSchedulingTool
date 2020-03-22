#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-03-14
import json
import entity_pb2
from google.protobuf import text_format

class Entity(list):
    
    def __init__(self, entype, demandid=-1, databaseid=-1, 
            name=None, desc=None, location=None,
            ncpu=None, mem=None, store=None):
        super(list, self).__init__()
        self.type = entype
        self.demandid = demandid
        self.databaseid = databaseid
        self.name = name
        self.desc = desc
        self.location = location
        self.ncpu = ncpu
        self.mem = mem
        self.store = store

def entity_str(entity, dep=0):
    typestr = entity.type
    itemstr = ''
    for item in entity:
        tmp = entity_str(item, dep+1)
        if tmp.strip() != '':
            itemstr += '\n' + tmp
    if itemstr.strip() != '':
        itemstr += '\n' + ' ' * 2 * dep
    return ' ' * 2 * dep + f'{typestr}({entity.name}):' \
            + f'[{itemstr}]'

def parse_json_to_entity(jsonObj, entype):

    def parse_App(jsonObj):
        entity = entity_pb2.Entity()
        entity.name = 'demand'
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


def queryResources(jsonObj):
    pass # 当前可用的entity


def fit(demands, resources):
    if demands.type != resources.type:
        raise Exception(f'demands.type: {demands.type} '
                        f'!= resources.type: {resources.type}')
    if demands.type in ['Devices', 'Workers', 'Applications']:
        return demands.name == resources.name
    elif demands.type in ['CloudNodes', 'EdgeServers']:
        return demands.store <= resources.store \
                and demands.ncpu <= resources.ncpu \
                and demands.mem <= resources.mem
    else:
        return bipartite_graph_matching(demands, resources)


def dfs(demand_idx, demand, resources, used, match, dfs_type, res):
    for resource_idx, resource in enumerate(resources):
        if bipartite_graph_match(demand, resource, dfs_type, res) and not used[resource_idx]:
            used[resource_idx] = True
            if match[resource_idx] == -1 or \
                    dfs(match[resource_idx], demand, resources, used, match, dfs_type):
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
            used = [0 for x in range(dn)]
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
            used = [0 for x in range(dn)]
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
            netnodes_used = [0 for x in range(netnodes_dn)]
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
            edgeservers_used = [0 for x in range(edgeservers_dn)]
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
            used = [0 for x in range(dn)]
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
            devices_used = [0 for x in range(devices_dn)]
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
            workers_used = [0 for x in range(workers_dn)]
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
            applications_used = [0 for x in range(applications_dn)]
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
    return res

def respose(match):
    pass # return match


def print_proto(proto):
    text = text_format.MessageToString(proto, as_utf8=True)
    print(text)

if __name__ == '__main__':
    with open('./demand.hrm') as f:
        jsonObj = json.loads(f.read())
        demands = receive(jsonObj)
        #  print_proto(demands)
    with open('./resource.prototxt') as f:
        resources = entity_pb2.Entity()
        text_format.Parse(f.read(), resources)
        #  print_proto(resources)
    print(schedule(demands, resources))
