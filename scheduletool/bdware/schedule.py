#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-14
import json
from scheduletool.bdware.query import QueryExecutor
from operator import itemgetter, attrgetter

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
            value, uint = storage.split(" ")
            if uint == "B":
                value = float(value)
            elif uint == "KB":
                value = 1000 * float(value)
            elif uint == "MB":
                value = 1000000 * float(value)
            elif uint == "GB":
                value = 1000000000 * float(value)
            elif uint == "TB":
                value = 1000000000000 * float(value)
            else:
                raise Exception("error unit: {}".format(uint))
            self.storage = value
            value, uint = traffic.split(" ")
            if uint == "B":
                value = float(value)
            elif uint == "KB":
                value = 1000 * float(value)
            elif uint == "MB":
                value = 1000000 * float(value)
            elif uint == "GB":
                value = 1000000000 * float(value)
            elif uint == "TB":
                value = 1000000000000 * float(value)
            else:
                raise Exception("error unit: {}".format(uint))
            self.traffic = value
        def __cmp__(self, other):
            if self.storage == other.storage:
                if self.traffic == other.traffic:
                    return 0
                elif self.traffic < other.traffic:
                    return -1
                else:
                    return 1
            elif self.storage < other.storage:
                return -1
            else:
                return 1

    query_exe = QueryExecutor()
    node_homes = []
    nodes = {}
    for idx, node in enumerate(node_infos):
        node_home = node["home"]
        node_homes.append(node_home)
        nodes[node_home] = {
            "contracts": [],
            "storage": node["storage"],
            "traffic": node["traffic"],
        }
        data = query_exe.queryNodeInfo(node_home)
        contracts = []
        for contract_data in data:
            contract = Contract(
                    contract_data["id"],
                    contract_data["storage"],
                    contract_data["traffic"])
            contracts.append(contract)
        contracts = sorted(contracts, key=attrgetter("storage", "traffic"))
        nodes[node_home]["contracts"] = contracts
    
    res = {}
    remain_contracts = []
    for home, node in nodes.items():
        res[home] = {
            "contracts": [],
            "storage": None,
            "traffic": None,
        }
        remain_sto = node["storage"] * threshold
        remain_tra = node["traffic"] * threshold
        idx = 0
        for contract in node["contracts"]:
            if remain_sto < contract.storage:
                break
            if remain_tra < contract.traffic:
                break
            remain_sto -= contract.storage
            remain_tra -= contract.traffic
            res[home]["contracts"].append(contract)
            idx += 1
        res[home]["storage"] = remain_sto
        res[home]["traffic"] = remain_tra
        remain_contracts.extend(node["contracts"][idx:])

    succ = True
    for contract in remain_contracts:
        succ = False
        for home, node in res.items():
            if node["storage"] >= contract.storage \
                    and node["traffic"] >= contract.traffic:
                res[home]["contracts"].append(contract)
                res[home]["storage"] -= contract.storage
                res[home]["traffic"] -= contract.traffic
                succ = True
                break
        if succ is False:
            break
    
    resp = {}
    if succ:
        for home, node in res.items():
            resp[home] = [c.cid for c in node["contracts"]]
    return json.dumps(resp)

if __name__ == "__main__":
    privateKey = "ab8c753378a031976cf2a848e57299240cdbbdecf36e726aa8a1e4a9fa9046e1"
    publicKey = "042ee9d52a0d31f1e4f9f16a636154179ed3386706add6439b778e7cc7792743b1a75076fb9682411a87ecef88652999f646a0a9b232ceecde59b5c39e7bb49f2f"

    nc_home = "http://127.0.0.1:1718"
    #  load_balancing_by_node_centor(nc_home, privateKey, publicKey)
    node_infos = [{
        "home": "http://127.0.0.1:8080/SCIDE/SCManager",
        "storage": 1019400000.0,
        "traffic": 100000.0
    }, {
        "home": "http://127.0.0.1:9090/SCIDE/SCManager",
        "storage": 1019400000.0,
        "traffic": 100000.0
    }]
    threshold = 0.8
    print(load_balancing_by_nodes(node_infos, threshold))
