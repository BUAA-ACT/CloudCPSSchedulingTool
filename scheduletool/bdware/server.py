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
from .proto import schedule_service_pb2_grpc
from .proto import schedule_service_pb2 as schedule_pb2

class ScheduleServicer(schedule_service_pb2_grpc.ScheduleServiceServicer):
    def __init__(self):
        pass
    
    def LoadBalancingByNodes(self, requests, content):
        node_infos = []
        for node_info_pb in requests.nodes:
            node_infos.append({
                "home": node_info_pb.home,
                "storage": node_info_pb.storage,
                "traffic": node_info_pb.traffic
            })
        threshold = requests.threshold 
        json = schedule.load_balancing_by_nodes(node_infos, threshold)
        res = schedule_pb2.LoadBalancingByNodesResponse()
        res.json_str = json
        return res

class ScheduleServer(object):
    def __init__(self):
        pass

    def _port_is_available(self, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(2)
            result = sock.connect_ex(('0.0.0.0', port))
        return result != 0

    def start(self, worker_num, port):
        if not self._port_is_available(port):
            raise SystemExit("Port already use: {}".format(port))
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
