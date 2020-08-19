#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-19
import sys
import grpc
from . import schedule
from concurrent import futures
import contextlib
import socket
from contextlib import closing
from .entity import Contract, Node, Cluster
from .proto import schedule_service_pb2_grpc
from .proto import schedule_service_pb2 as schedule_pb2

class ScheduleServicer(schedule_service_pb2_grpc.ScheduleServiceServicer):
    def __init__(self):
        pass
    
    def _parse_clusters_pb(self, pb_clusters):
        clusters = []
        for pb_cluster in pb_clusters:
            nodes = {}
            for pb_node in pb_cluster.nodes:
                nodes[pb_node.home] = Node(pb_node.home, pb_node.storage, pb_node.traffic)
            clusters.append(Cluster(pb_cluster.name, nodes))
        return clusters

    def _parse_contract_pb(self, pb_contract):
        contract = Contract(None, pb_contract.storage, pb_contract.traffic)
        return contract

    def QueryDeployedCluster(self, requests, content):
        clusters = self._parse_clusters_pb(requests.clusters)
        contract = self._parse_contract_pb(requests.contract)
        threshold = requests.threshold
        cluster_name = schedule.query_deployed_cluster(clusters, threshold, contract)
        resp = schedule_pb2.QueryDeployedClusterResponse()
        resp.error_code = 0
        if cluster_name is None:
            resp.error_code = -1
            return resp
        resp.cluster_name = cluster_name
        return resp

    def LoadBalancingByNodes(self, requests, content):
        clusters = self._parse_clusters_pb(requests.clusters)
        threshold = requests.threshold 
        transfers = schedule.load_balancing_by_nodes(clusters, threshold)
        resp = schedule_pb2.LoadBalancingByNodesResponse()
        resp.error_code = 0
        if transfers is None:
            resp.error_code = -1
            return resp
        for transfer in transfers:
            resp.transfers.append(
                    schedule_pb2.ContractTransfer(
                        contract_id=transfer["cid"],
                        cluster_src=transfer["src"],
                        cluster_dst=transfer["dst"]))
        return resp

class ScheduleServer(object):
    def __init__(self):
        pass

    def _port_is_available(self, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(2)
            result = sock.connect_ex(('0.0.0.0', port))
        return result != 0

    def start(self, worker_num, port):
        #if not self._port_is_available(port):
        #    raise SystemExit("Port already use: {}".format(port))
        server = grpc.server(
                futures.ThreadPoolExecutor(max_workers=worker_num))
        schedule_service_pb2_grpc.add_ScheduleServiceServicer_to_server(
                ScheduleServicer(), server)
        server.add_insecure_port('[::]:{}'.format(port))
        server.start()
        print("Server start on {}".format(port))
        server.wait_for_termination()

if __name__ == "__main__":
    server = ScheduleServer()
    server.start(2, 18080)
