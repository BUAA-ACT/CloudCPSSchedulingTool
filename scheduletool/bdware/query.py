#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-03-14
import json
import scheduletool.bdware.bdcaller as bdcaller
import requests
from scheduletool.bdware.sm2_util import JsSM2Executor as SM2Executor

class QueryExecutor(object):
    def __init__(self):
        self.caller_ = bdcaller.BDCaller()
        
    def queryNodesConnWithNodeCenter(self, nc_home, publicKey, privateKey):
        sm2 = SM2Executor(privateKey=privateKey, publicKey=publicKey)
        content = "action=listCMInfo&pubKey=" + publicKey
        signature = sm2.sign(content)

        if sm2.verify(content, signature) is False:
            raise Exception("verify signature failed.")

        params = {
            "action": "listCMInfo",
            "pubKey": publicKey,
            "sign": signature,
        }
        r = requests.get("{}/NodeCenterWS/SCIDE/SCManager".format(nc_home), params=params)
        resp = json.loads(r.content)
        print(json.dumps(resp, sort_keys=True, indent=4, separators=(',', ': ')))
        
        nodes = []
        #TODO 
        return nodes
    
    def queryNodeInfo(self, url):
        params = {
            "action": "listContractProcess",
        }
        contracts = self.caller_.callAPI(params, home=url)
        
        contract_infos = []
        for contract in contracts:
            info = {
                "id": contract["id"],
                "name": contract["name"],
                "port": contract["port"],
                "storage": contract["storage"],
                "times": contract["times"],
                "traffic": contract["traffic"],
                "type": contract["type"],
            }
            contract_infos.append(info)
        return contract_infos
