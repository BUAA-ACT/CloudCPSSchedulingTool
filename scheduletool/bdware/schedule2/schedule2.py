#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0

"""
[{
 "NodeID": "xxxxxx",
 "NodeFreeResourceInfo":"...jsonString...",
 "NodeContractResourceInfo":"...jsonString..."
}, {
 "NodeInfo": "...jsonString...",
 "NodeFreeResourceInfo":"...jsonString...",
 "NodeContractResourceInfo":"...jsonString..."
},
...
{
 "NodeInfo": "...jsonString...",
 "NodeFreeResourceInfo":"...jsonString...",
 "NodeContractResourceInfo":"...jsonString..."
}]
"""
import json
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M', level=logging.INFO)

def parse_json(json_obj):
    nodes = []
    for node in json_obj:
        nid = node["NodeID"]
        threshold = node["threshold"]
        NodeFreeResourceInfo = node["NodeFreeResourceInfo"]
        free = {
            "mem": float(NodeFreeResourceInfo["freeMEM"].split(" ")[0]),
            "cpu": float(NodeFreeResourceInfo["freeCPU"].split("%")[0]),
        }
        NodeContractResourceInfo = node["NodeContractResourceInfo"]
        contracts = []
        for c in NodeContractResourceInfo:
            contracts.append(Contract(
                cid=c["id"],
                mem=float(c["rss"].split(" ")[0]),
                cpu=float(c["cpu"].split("%")[0])))
        nodes.append(Node(
            nid=nid, 
            free=free, 
            contracts=contracts,
            threshold=threshold))
    return nodes

class Contract(object):
    def __init__(self, cid, mem, cpu):
        self.cid = cid
        self.mem = mem
        self.cpu = cpu

class Node(object):
    def __init__(self, nid, free, contracts, threshold):
        self.nid = nid
        self.mem = free["mem"]
        self.cpu = free["cpu"]
        self.threshold = threshold
        self.contracts = {c.cid: c for c in contracts}
        self.tot_mem = self.mem
        self.tot_cpu = self.cpu
        for c in self.contracts.values():
            self.tot_mem += c.mem
            self.tot_cpu += c.cpu
        self.tonodes = {} # contract.id : node
        self.backnodes = {} # contract.id : nodes
        self.rest = 1 - self.threshold


    def min_num_to_mem(self):
        mem = self.tot_mem * self.rest - self.mem
        contracts = list(self.contracts.values())
        contracts.sort(key=lambda x:x.mem, reverse=True)
        for idx, contract in enumerate(contracts):
            mem -= contract.mem
            if mem <= 0:
                return idx + 1

    def min_num_to_cpu(self):
        cpu = self.tot_cpu * self.rest - self.cpu
        contracts = list(self.contracts.values())
        contracts.sort(key=lambda x:x.cpu, reverse=True)
        for idx, contract in enumerate(contracts):
            cpu -= contract.cpu
            if cpu <= 0:
                return idx + 1

    def add_tonode(self, cid, nid):
        if cid not in self.tonodes:
            self.tonodes[cid] = set()
        if nid in self.tonodes[cid]:
            raise Exception("nid({}) already exists in tonodes".format(nid))
        self.tonodes[cid].add(nid)

    def remove_tonode(self, cid, nid):
        if nid not in self.tonodes[cid]:
            raise Exception("nid({}) not in tonodes".format(nid))
        self.tonodes[cid].remove(nid)

    def add_backnode(self, cid, nid):
        if cid not in self.backnodes:
            self.backnodes[cid] = set()
        if nid in self.backnodes[cid]:
            raise Exception("nid({}) already exists in backnodes".format(nid))
        self.backnodes[cid].add(nid)

    def rm_backnode(self, cid, nid):
        if nid not in self.backnodes[cid]:
            raise Exception("nid({}) not in backnodes".format(nid))
        self.backnodes[cid].remove(nid)

    def remove_contract(self, cid):
        if cid not in self.contracts:
            raise Exception("cid({}) not in Node({})".format(cid, self.nid))
        contract = self.contracts.pop(cid)
        self.mem += contract.mem
        self.cpu += contract.cpu
        self.tonodes.pop(cid)
        return contract

    def add_contract(self, contract):
        if contract.cid in self.contracts:
            raise Exception("cid({}) already exists in Node({})".format(contract.cid, self.nid))
        self.mem -= contract.mem
        self.cpu -= contract.cpu
        self.contracts[contract.cid] = contract

    def exceed(self):
        return self.tot_mem * self.rest > self.mem or self.tot_cpu * self.rest > self.cpu

class Graph(object):
    def __init__(self, nodes):
        self.contract2nodes = {}
        for node in nodes:
            for cid, contract in node.contracts.items():
                if cid not in self.contract2nodes:
                    self.contract2nodes[cid] = set()
                self.contract2nodes[cid].add(node.nid)
                for tonode in nodes:
                    if tonode.nid == node.nid:
                        continue
                    if cid not in tonode.contracts:
                        node.add_tonode(cid, tonode.nid)
            logging.debug("nid[{}] tonode: {}".format(node.nid, node.tonodes))
        self.nodes = {n.nid: n for n in nodes}
        self.exceed_nodes = set()
        for nid, node in self.nodes.items():
            if node.exceed():
                self.exceed_nodes.add(nid)
        self.transfers = {}

    def transfer(self, src_nid, dst_nid, cid, add=True):
        src_node = self.nodes[src_nid]
        dst_node = self.nodes[dst_nid]
        logging.debug("nid[{}] tonode: {}".format(src_nid, src_node.tonodes.get(cid)))
        logging.debug("nid[{}] tonode: {}".format(dst_nid, dst_node.tonodes.get(cid)))
        self.update_node_tonodes(src_node, dst_node, cid)
        self.update_node_backnodes(src_node, dst_node, cid)
        self.update_node_contracts(src_node, dst_node, cid)
        self.update_exceed_nodes(src_node, dst_node)
        self.update_transfer(src_node, dst_node, cid, add)
        logging.debug("nid[{}] tonode: {}".format(src_nid, src_node.tonodes.get(cid)))
        logging.debug("nid[{}] tonode: {}".format(dst_nid, dst_node.tonodes.get(cid)))
        logging.debug("===========")

    def update_transfer(self, src_node, dst_node, cid, add):
        src_nid = src_node.nid
        dst_nid = dst_node.nid
        if add:
            if cid in self.transfers:
                raise Exception("cid({}) already exists in transfers".format(cid))
            self.transfers[cid] = {
                "src": src_nid,
                "dst": dst_nid,
            }
        else:
            if cid not in self.transfers:
                raise Exception("cid({}) not exists in transfers".format(cid))
            self.transfers.pop(cid)
    
    def update_exceed_nodes(self, src_node, dst_node):
        src_nid = src_node.nid
        dst_nid = dst_node.nid
        logging.debug("update_exceed_nodes: {} => {}".format(src_nid, dst_nid))
        if src_nid in self.exceed_nodes and not src_node.exceed():
            self.exceed_nodes.remove(src_nid)
        if dst_nid not in self.exceed_nodes and dst_node.exceed():
            self.exceed_nodes.add(dst_nid)

    def update_node_contracts(self, src_node, dst_node, cid):
        logging.debug("update_node_contracts: [{}] {} => {}".format(cid, src_node.nid, dst_node.nid))
        contract = src_node.remove_contract(cid)
        dst_node.add_contract(contract)

    def update_node_tonodes(self, src_node, dst_node, cid):
        logging.debug("update_node_tonode: [{}] {} => {}".format(cid, src_node.nid, dst_node.nid))
        if cid not in src_node.tonodes:
            src_node.tonodes[cid] = set()
        if cid not in dst_node.tonodes:
            dst_node.tonodes[cid] = set()
        src_node.tonodes[cid], dst_node.tonodes[cid] = dst_node.tonodes[cid], src_node.tonodes[cid]
        dst_node.remove_tonode(cid, dst_node.nid)
        dst_node.add_tonode(cid, src_node.nid)

    def update_node_backnodes(self, src_node, dst_node, cid):
        src_nid = src_node.nid
        dst_nid = dst_node.nid
        logging.debug("update_node_backnodes: [{}] {} => {}".format(cid, src_nid, dst_nid))
        if src_nid not in self.contract2nodes[cid]:
            raise Exception("Failed to transfer: nid[{}] not in contract2nodes".format(src_nid))
        self.contract2nodes[cid].remove(src_nid)
        self.contract2nodes[cid].add(dst_nid)
        if cid not in src_node.backnodes:
            src_node.backnodes[cid] = set()
        if cid not in dst_node.backnodes:
            dst_node.backnodes[cid] = set()
        for nid in src_node.backnodes[cid]:
            node = self.nodes[nid]
            node.remove_tonode(src_nid)
            node.add_tonode(dst_nid)
        src_node.backnodes[cid], dst_node.backnodes[cid] = dst_node.backnodes[cid], src_node.backnodes[cid]

    def check(self):
        return len(self.exceed_nodes) == 0

    def transfer_already_exists(self, cid):
        return cid in self.transfers

    def min_num_to_transfer(self):
        count = 0
        for exceed_nid in self.exceed_nodes:
            min_count = max(
                    self.nodes[exceed_nid].min_num_to_mem(),
                    self.nodes[exceed_nid].min_num_to_cpu())
            count += min_count
        return count

def star(graph):
    return graph.min_num_to_transfer()

def IDAstar(graph, depth, max_depth):
    logging.debug("IDA*: depth[{}] max_depth[{}]".format(depth, max_depth))
    if graph.check():
        return True
    Astar = star(graph)
    logging.debug("Star: {}".format(Astar))
    if Astar + depth > max_depth:
        logging.debug("Astar({}) + depth({}) > max_depth({})".format(Astar, depth, max_depth))
        return False
    logging.debug("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    logging.debug("exceed_nids: {}".format(graph.exceed_nodes))
    for exceed_nid in graph.exceed_nodes:
        exceed_node = graph.nodes[exceed_nid]
        logging.debug("exceed_node: {}".format(exceed_node.nid))
        for cid in exceed_node.contracts:
            tonodes = exceed_node.tonodes[cid]
            for dst_nid in tonodes:
                if graph.transfer_already_exists(cid):
                    continue
                logging.debug(" > {} {} {}".format(exceed_nid, dst_nid, cid))
                graph.transfer(exceed_nid, dst_nid, cid, add=True)
                if IDAstar(graph, depth + 1, max_depth):
                    return True
                logging.debug(" < {} {} {}".format(dst_nid, exceed_nid, cid))
                graph.transfer(dst_nid, exceed_nid, cid, add=False)

def schedule(json_obj):
    nodes = parse_json(json_obj)
    graph = Graph(nodes)

    depth = 0
    max_depth = 5
    while depth <= max_depth and not IDAstar(graph, 0, depth):
        depth += 1
        logging.info("try depth: {}".format(depth))
    
    transfers = [{
        "NodeContractID": key,
        "SourceNode": value["src"],
        "DestinationNode": value["dst"]
    } for key, value in graph.transfers.items()]
    
    return {"result": transfers}

if __name__ == "__main__":
    with open("test.txt2") as f:
        t = f.read()
    json_obj = json.loads(t)
    transfers = schedule(json_obj)
    print(len(transfers))
    print(json.dumps(transfers, indent=2, separators=(',', ':')))
