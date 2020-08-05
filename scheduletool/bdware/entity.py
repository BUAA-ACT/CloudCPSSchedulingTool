#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-08-03
from .query import QueryExecutor
from .util import string_with_uint_to_float
from operator import itemgetter, attrgetter
import logging

class Cluster(object):
    def __init__(self, name, nodes):
        self.name = name
        if not isinstance(nodes, dict):
            raise Exception("error type")

        self.nodes = nodes
        for home, node in nodes.items():
            if not isinstance(node, Node):
                raise Exception("error type")
        self.contracts = {}
        self.remain_storage = None
        self.remain_traffic = None

    def init(self, threshold):
        cluster_contract = None
        tot_contracts = {}
        for node in self.nodes.values():
            node.init(threshold)
            node_contracts = set([c.cid for c in node.contracts.values()])
            if cluster_contract is None:
                cluster_contract = node_contracts
            else:
                cluster_contract &= node_contracts
            for contract in node.contracts.values():
                if contract.cid not in tot_contracts:
                    tot_contracts[contract.cid] = contract
        for cid in cluster_contract:
            self.contracts[cid] = tot_contracts[cid]
        logging.debug("Cluster({}): {}".format(self.name, self.contracts.keys()))
    
    def calculate_storage_and_traffic(self):
        self.remain_storage = min([node.remain_storage for node in self.nodes.values()])
        self.remain_traffic = min([node.remain_traffic for node in self.nodes.values()])

    def max_storage_contract(self):
        max_storage = 0
        contract = None
        for c in self.contracts.values():
            if max_storage < c.storage:
                max_storage = c.storage
                contract = c
        return contract

    def max_traffic_contract(self):
        max_traffic = 0
        contract = None
        for c in self.contracts.values():
            if max_traffic < c.traffic:
                max_traffic = c.traffic
                contract = c
        return contract

    def remove_contract(self, cid):
        if cid not in self.contracts:
            raise Exception("cid({}) not in Cluster({})".format(cid, self.name))
        for node in self.nodes.values():
            node.remove_contract(cid)
        contract = self.contracts.pop(cid)

    def add_contract(self, contract):
        if contract.cid in self.contracts:
            logging.warning("contract({}) already exists in cluster({})".format(contract.cid, self.name))
            # we assume that contractID is globally unique
            return
        for node in self.nodes.values():
            node.add_contract(contract)
        self.contracts[contract.cid] = contract

    def check_can_add_contract(self, contract):
        for node in self.nodes.values():
            if not node.check_can_add_contract(contract):
                return False
        return True

    def __cmp__(self, other):
        if self.remain_storage == other.remain_storage:
            if self.remain_traffic == other.remain_traffic:
                return 0
            elif self.remain_traffic < other.remain_traffic:
                return -1
            else:
                return 1
        elif self.remain_storage < other.remain_storage:
            return -1
        else:
            return 1

class Node(object):
    def __init__(self, home, storage, traffic):
        self.home = home
        if isinstance(storage, str):
            self.storage = string_with_uint_to_float(storage)
        elif isinstance(storage, float):
            self.storage = storage
        else:
            raise Exception("error type: {}".format(type(storage)))

        if isinstance(traffic, str):
            self.traffic = string_with_uint_to_float(traffic)
        elif isinstance(traffic, float):
            self.traffic = traffic
        else:
            raise Exception("error type: {}".format(type(traffic)))
        logging.debug("[Node] home: {}, storage: {}, traffic: {}"
                .format(home, self.storage, self.traffic))
        self.threshold = None
        self.contracts = None
        self.used_storage = None
        self.used_traffic = None

    def init(self, threshold):
        self.threshold = threshold
        query_exe = QueryExecutor()
        data = query_exe.queryNodeInfo(self.home)
        self.contracts = {}
        self.used_storage = 0
        self.used_traffic = 0
        for contract_data in data:
            contract = Contract(
                    contract_data["id"],
                    contract_data["storage"],
                    contract_data["traffic"])
            self.used_storage += contract.storage
            self.used_traffic += contract.traffic
            self.contracts[contract.cid] = contract
        logging.debug("Node({}): {}".format(self.home, self.contracts.keys()))

    def remove_contract(self, cid):
        if cid not in self.contracts:
            raise Exception("cid({}) not in Node({})".format(cid, self.home))
        contract = self.contracts.pop(cid)
        self.used_storage -= contract.storage
        self.used_traffic -= contract.traffic

    def add_contract(self, contract):
        self.used_storage += contract.storage
        self.used_traffic += contract.traffic
        self.contracts[contract.cid] = contract

    def check_can_add_contract(self, contract):
        storage = self.storage 
        traffic = self.traffic
        if self.threshold is not None:
            storage *= storage
            traffic *= traffic
        if self.used_storage + contract.storage > storage:
            return False
        if self.used_traffic + contract.traffic > traffic:
            return False
        return True

    @property
    def remain_storage(self):
        return self.storage * self.threshold - self.used_storage

    @property
    def remain_traffic(self):
        return self.traffic * self.threshold - self.used_traffic

class Contract(object):
    def __init__(self, cid, storage, traffic):
        self.cid = cid
        logging.debug("[Contract] cid: {}, storage: {}, traffic: {}"
                .format(cid, storage, traffic))
        if isinstance(storage, str):
            self.storage = string_with_uint_to_float(storage)
        elif isinstance(storage, float):
            self.storage = storage
        else:
            raise Exception("error type: {}".format(type(storage)))

        if isinstance(traffic, str):
            self.traffic = string_with_uint_to_float(traffic)
        elif isinstance(traffic, float):
            self.traffic = traffic
        else:
            raise Exception("error type: {}".format(type(traffic)))
        logging.debug("[Contract] cid: {}, storage: {}, traffic: {}"
                .format(cid, self.storage, self.traffic))

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
