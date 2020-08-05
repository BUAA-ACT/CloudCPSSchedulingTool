#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-08-05

def string_with_uint_to_float(s):
    if not isinstance(s, str):
        raise Exception("not str")
    value, uint = s.split(" ")
    uint_order = {
        "B": 1,
        "KB": 1e3,
        "MB": 1e6,
        "GB": 1e9,
        "TB": 1e12,
    }
    if uint not in uint_order:
        raise Exception("error unit: {}".format(uint))
    return uint_order[uint] * float(value)
