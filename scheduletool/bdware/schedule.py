#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-14
import json
from .query import QueryExecutor
from .entity import Contract, Node, Cluster
from operator import itemgetter, attrgetter
import logging

def load_balancing_by_node_centor(node_center, privateKey, publicKey):
    q = QueryExecutor()
    data = q.queryNodesConnWithNodeCenter(
            nc_home=node_center, publicKey=publicKey, privateKey=privateKey)
    print(data)
    # TODO
    return None

def query_deployed_cluster(clusters, threshold, contract):
    for cluster in clusters:
        cluster.init(threshold)
        cluster.calculate_storage_and_traffic()
    
    for cluster in clusters:
        if cluster.remain_storage >= contract.storage \
                and cluster.remain_traffic >= contract.traffic:
            logging.info("Succ to schedule: {}".format(cluster.name))
            return cluster.name

    logging.error("Failed to schedule.")
    return None

def _print_cluster_state(clusters):
    logging.debug("===== state =====")
    for cluster in clusters:
        logging.debug("Cluster({}): {}".format(cluster.name, cluster.contracts.keys()))
    logging.debug("=================")

def load_balancing_by_nodes(clusters, threshold):
    tot_contract_count = 0
    for cluster in clusters:
        cluster.init(threshold)
        logging.debug("succ init cluster: {}".format(cluster.name))
        tot_contract_count += len(cluster.contracts)

    transfers = []
    step = 0
    while step < tot_contract_count:
        for cluster in clusters:
            cluster.calculate_storage_and_traffic()
        _print_cluster_state(clusters)
        index = 0
        for cluster in clusters:
            logging.debug("cluster({}) remain_storage: {}, remain_traffic: {}"
                    .format(cluster.name, cluster.remain_storage, cluster.remain_traffic))
            if cluster.remain_storage < 0 \
                    or cluster.remain_traffic < 0:
                break
            index += 1
        if index == len(clusters):
            logging.info("Succ to transfer")
            break

        contract = None
        if clusters[index].remain_storage < 0:
            contract = cluster.max_storage_contract()
        elif clusters[index].remain_traffic < 0:
            contract = cluster.max_traffic_contract()
        logging.debug("contract(id: {}, storage: {}, traffic: {}) "
                "in cluster({}) should be transfered".format(
                    contract.cid, contract.storage, contract.traffic,
                    clusters[index].name))

        transfer = None
        for idx, cluster in enumerate(clusters):
            if idx != index:
                if cluster.check_can_add_contract(contract):
                    logging.debug("try add contract(cid: {}, storage: {}, traffic: {}) to cluster({})"
                            .format(contract.cid, contract.storage, contract.traffic, cluster.name))
                    cluster.add_contract(contract)
                    logging.debug("try rm contract(cid: {}, storage: {}, traffic: {}) from cluster({})"
                            .format(contract.cid, contract.storage, contract.traffic, clusters[index].name))
                    clusters[index].remove_contract(contract.cid)
                    transfer = {
                        "cid": contract.cid,
                        "src": cluster.name,
                        "dst": clusters[index].name,
                    }
                    logging.info("Succ to transfer one contract: {}".format(transfer))
                    break

        if transfer is None:
            logging.debug("Failed to transfer.")
            break
        transfers.append(transfer)
        step += 1
    
    if step >= tot_contract_count:
        return None
    return transfers

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
