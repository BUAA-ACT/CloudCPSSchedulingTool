#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-20
import sys
import json
import grpc
from .proto import schedule_service_pb2 as schedule_pb2
from .proto import schedule_service_pb2_grpc as schedule_service_pb2_grpc

class ScheduleClient(object):
    def __init__(self):
        self._channel = None
        self._stub = None

    def connect(self, endpoints):
        options = [('grpc.max_receive_message_length', 512 * 1024 * 1024),
                   ('grpc.max_send_message_length', 512 * 1024 * 1024),
                   ('grpc.lb_policy_name', 'round_robin')]
        g_endpoint = 'ipv4:{}'.format(','.join(endpoints))
        self._channel = grpc.insecure_channel(g_endpoint, options=options)
        self._stub = schedule_service_pb2_grpc.ScheduleServiceStub(self._channel)

    def query_lb_by_nodes(self, clusters, threshold):
        req = schedule_pb2.LoadBalancingByNodesRequest()
        req.threshold = threshold
        for cluster in clusters:
            pb_cluster = schedule_pb2.ClusterInfo()
            pb_cluster.name = cluster["name"]
            for node in cluster["nodes"]:
                pb_node = schedule_pb2.NodeInfo()
                pb_node.home = node["home"]
                pb_node.storage = node["storage"]
                pb_node.traffic = node["traffic"]
                pb_cluster.nodes.append(pb_node)
            req.clusters.append(pb_cluster)
        resp = self._stub.LoadBalancingByNodes(req)
        if resp.error_code != 0:
            return None
        transfers = []
        for pb_transfer in resp.transfers:
            transfers.append({
                "contract_id": pb_transfer.contract_id,
                "cluster_src": pb_transfer.cluster_src,
                "cluster_dst": pb_transfer.cluster_dst,
            })
        return transfers

if __name__ == "__main__":
    client = ScheduleClient()
    client.connect(["127.0.0.1:18080"])
    clusters = [{
        "name": "cluster1",
        "nodes": [{
            "home": "http://127.0.0.1:8080/SCIDE/SCManager",
            "storage": "1 MB",
            "traffic": "2 MB",
        }],
    }, {
        "name": "cluster2",
        "nodes": [{
            "home": "http://127.0.0.1:9090/SCIDE/SCManager",
            "storage": "1 MB",
            "traffic": "2 MB",
        }],
    }]
    threshold = 0.8
    transfers = client.query_lb_by_nodes(clusters, threshold)
    print(json.dumps(transfers, indent=4, separators=(',', ':')))
