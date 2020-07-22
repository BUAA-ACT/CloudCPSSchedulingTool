#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-13
import json
import requests

class BDCaller(object):
    def __init__(self, home=None):
        self.home_ = home

    def callAPI(self, params, home=None):
        if home is None:
            home = self.home_
        if home is None:
            raise Exception("params [home] can not be None")
        r = requests.get(home, params=params)
        resp = json.loads(r.content)
        data = json.loads(resp["data"])
        return data

    def callContract(self, params, home=None):
        if home is None:
            home = self.home_
        if home is None:
            raise Exception("params [home] can not be None")
        r = requests.get(home, params=params)
        resp = json.loads(r.content)
        data = json.loads(resp["data"])
        result = json.loads(data["result"])
        return result
