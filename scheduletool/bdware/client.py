#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-20
import sys
sys.path.append("./proto")
import grpc
import scheduletool.bdware.proto.schedule_service_pb2 as schedule_pb2
import scheduletool.bdware.proto.schedule_service_pb2_grpc as schedule_service_pb2_grpc

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

    def query_lb_by_nodes(self, node_infos, threshold):
        req = schedule_pb2.LoadBalancingByNodesRequest()
        req.threshold = threshold
        for node_info in node_infos:
            node_info_pb = schedule_pb2.NodeInfo()
            node_info_pb.home = node_info["home"]
            node_info_pb.storage = node_info["storage"]
            node_info_pb.traffic = node_info["traffic"]
            req.nodes.append(node_info_pb)
        resp = self._stub.LoadBalancingByNodes(req)
        json_str = resp.json_str
        return json_str

if __name__ == "__main__":
    client = ScheduleClient()
    client.connect(["127.0.0.1:18080"])
    node_infos = [{
        "home": "http://127.0.0.1:8080/SCIDE/SCManager",
        "storage": 101940000000,
        "traffic": 200000
    }, {
        "home": "http://127.0.0.1:9090/SCIDE/SCManager",
        "storage": 201440000000,
        "traffic": 200000,
    }]
    threshold = 0.8
    json_str = client.query_lb_by_nodes(node_infos, threshold)
    print(json_str)
