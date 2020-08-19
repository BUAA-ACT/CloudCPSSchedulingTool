#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-20
import sys
import grpc
import json
from scheduletool.bdware.client import ScheduleClient

if __name__ == "__main__":
    client = ScheduleClient()
    client.connect(["127.0.0.1:18067"])
    clusters = [{
        "name": "cluster1",
        "nodes": [{
            "home": "http://127.0.0.1:8080/SCIDE/SCManager",
            "storage": "1 GB",
            "traffic": "20 MB",
        }],
    }, {
        "name": "cluster2",
        "nodes": [{
            "home": "http://127.0.0.1:9090/SCIDE/SCManager",
            "storage": "135 MB",
            "traffic": "120 B",
        }],
    }]
    threshold = 0.8
    transfers = client.query_lb_by_nodes(clusters, threshold)
    print(json.dumps(transfers, indent=4, separators=(',', ':')))

    contract = {
        "storage": "1 MB",
        "traffic": "1 B",
    }
    cluster_name = client.query_deployed_cluster(clusters, threshold, contract)
    print(cluster_name)
