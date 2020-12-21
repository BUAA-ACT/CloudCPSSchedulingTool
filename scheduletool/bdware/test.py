#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-08
import json
with open("test.txt2") as f:
    a = f.read()
print(json.dumps(json.loads(a)))
