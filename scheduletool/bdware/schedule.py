#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-14
import json
from query import QueryExecutor

def load_balancing_by_node_centor(node_center, privateKey, publicKey):
    q = QueryExecutor()
    data = q.queryNodesConnWithNodeCenter(
            nc_home=node_center, publicKey=publicKey, privateKey=privateKey)
    print(data)
    # TODO
    return None

def load_balancing_by_nodes(node_infos, threshold):
    class Contract(object):
        def __init__(self, cid, storage, traffic):
            self.cid = cid
            #TODO
            self.storage = float(storage.split(" ")[0])
            self.traffic = float(traffic.split(" ")[0])

    query_exe = QueryExecutor()
    home_list = []
    storage_list = []
    traffic_list = []
    storage_rest = []
    traffic_rest = []
    each_node_contract_list = []
    node_size = len(node_infos)
    for idx, node in enumerate(node_infos):
        node_home = node["home"]
        home_list.append(node_home)
        data = query_exe.queryNodeInfo(node_home)
        contract_list = []
        tot_storage = 0
        tot_traffic = 0
        for contract_data in data:
            contract = Contract(
                    contract_data["id"],
                    contract_data["storage"],
                    contract_data["traffic"])
            tot_storage += contract.storage
            tot_traffic += contract.traffic
            contract_list.append(contract)
        storage_list.append(node["storage"])
        traffic_list.append(node["traffic"])
        storage_rest.append((idx, node["storage"] - tot_storage))
        traffic_rest.append((idx, node["traffic"] - tot_traffic))
        each_node_contract_list.append(contract_list)
        #  print(json.dumps(data, indent=2, separators=(',', ':')))

    ok = _schedule_for_storage(storage_list,
            traffic_list, storage_rest,
            traffic_rest, threshold, 
            each_node_contract_list)
    if not ok:
        return ""

    ok = _schedule_for_traffic(storage_list,
            traffic_list, storage_rest,
            traffic_rest, threshold,
            each_node_contract_list)
    if not ok:
        return ""

    resp = []
    for contract_list in each_node_contract_list:
        resp.append([contract.cid for contract in contract_list])
    
    return json.dumps(resp)

def _schedule_for_storage(storage_list,
        traffic_list, storage_rest, traffic_rest,
        threshold, each_node_contract_list):
    def takeSecond(elem):
        return elem[1]

    def transfer(src_node_idx, src_rest_idx,
            dest_node_idx, dest_rest_idx):
        src_sto = storage_list[src_node_idx]
        src_tra = traffic_list[src_node_idx]
        src_rest_sto = storage_rest[src_rest_idx][1]
        src_rest_tra = traffic_rest[src_rest_idx][1]
        dest_sto = storage_list[dest_node_idx]
        dest_tra = traffic_list[dest_node_idx]
        dest_rest_sto = storage_rest[dest_node_idx][1]
        dest_rest_tra = traffic_rest[dest_node_idx][1]
        while src_rest_sto < threshold * src_sto:
            contract = each_node_contract_list[src_rest_idx][0]
            if dest_rest_sto - contract.storage > threshold * dest_sto \
                    and dest_rest_tra - contract.traffic > threshold * dest_tra:
                # ok to transfer
                storage_rest[src_rest_idx][1] += contract.storage
                traffic_rest[src_rest_idx][1] += contract.traffic
                storage_rest[dest_node_idx][1] -= contract.storage
                traffic_rest[dest_node_idx][1] -= contract.traffic
                src_rest_sto += contract.storage
                src_rest_tra += contract.traffic
                dest_rest_sto -= contract.storage
                dest_rest_tra -= contract.traffic
                each_node_contract_list[src_node_idx].append(contract)
                each_node_contract_list[dest_node_idx].pop(0)
            else:
                break
        return src_rest_sto > threshold * src_sto

    storage_rest.sort(key=takeSecond)
    index = len(storage_rest) - 1
    for rest in reversed(storage_rest):
        node_idx, rest_sto = rest
        if rest_sto > threshold * storage_list[node_idx]:
            break
        # transfer...
        ok = False
        for tf_idx in range(index):
            ret = transfer(index, node_idx,
                    storage_rest[tf_idx][0], tf_idx)
            if ret:
                ok = True
                break
        if not ok:
            return False
    return True

def _schedule_for_traffic(storage_list,
        traffic_list, storage_rest, traffic_rest,
        threshold, each_node_contract_list):
    def takeSecond(elem):
        return elem[1]
    
    def transfer(src_node_idx, src_rest_idx,
            dest_node_idx, dest_rest_idx):
        src_sto = storage_list[src_node_idx]
        src_tra = traffic_list[src_node_idx]
        src_rest_sto = storage_rest[src_rest_idx][1]
        src_rest_tra = traffic_rest[src_rest_idx][1]
        dest_sto = storage_list[dest_node_idx]
        dest_tra = traffic_list[dest_node_idx]
        dest_rest_sto = storage_rest[dest_node_idx][1]
        dest_rest_tra = traffic_rest[dest_node_idx][1]
        while src_rest_tra < threshold * src_tra:
            contract = each_node_contract_list[src_rest_idx][0]
            if dest_rest_sto - contract.storage > threshold * dest_sto \
                    and dest_rest_tra - contract.traffic > threshold * dest_tra:
                # ok to transfer
                storage_rest[src_rest_idx][1] += contract.storage
                traffic_rest[src_rest_idx][1] += contract.traffic
                storage_rest[dest_node_idx][1] -= contract.storage
                traffic_rest[dest_node_idx][1] -= contract.traffic
                src_rest_sto += contract.storage
                src_rest_tra += contract.traffic
                dest_rest_sto -= contract.storage
                dest_rest_tra -= contract.traffic
                each_node_contract_list[src_node_idx].append(contract)
                each_node_contract_list[dest_node_idx].pop(0)
            else:
                break
        return src_rest_tra > threshold * src_tra

    traffic_rest.sort(key=takeSecond)
    index = len(traffic_rest) - 1
    for rest in reversed(traffic_rest):
        node_idx, rest_tra = rest
        if rest_tra > threshold * traffic_list[node_idx]:
            break
        # transfer...
        ok = False
        for tf_idx in range(index):
            ret = transfer(index, node_idx,
                    traffic_rest[tf_idx][0], tf_idx)
            if ret:
                ok = True
                break
        if not ok:
            return False
    return True

if __name__ == "__main__":
    privateKey = "ab8c753378a031976cf2a848e57299240cdbbdecf36e726aa8a1e4a9fa9046e1"
    publicKey = "042ee9d52a0d31f1e4f9f16a636154179ed3386706add6439b778e7cc7792743b1a75076fb9682411a87ecef88652999f646a0a9b232ceecde59b5c39e7bb49f2f"

    nc_home = "http://127.0.0.1:1718"
    #  load_balancing_by_node_centor(nc_home, privateKey, publicKey)
    node_infos = [{
        "home": "http://127.0.0.1:8080/SCIDE/SCManager",
        "storage": 100.0,
        "traffic": 100.0
    }, {
        "home": "http://127.0.0.1:9090/SCIDE/SCManager",
        "storage": 100.0,
        "traffic": 100.0
    }]
    threshold = 0.2
    print(load_balancing_by_nodes(node_infos, threshold))
