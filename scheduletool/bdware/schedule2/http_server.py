#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0

from flask import Flask, request
import schedule2
import logging
app = Flask(__name__)

@app.route('/', methods=["POST"])
def run():
    return schedule2.schedule(request.json)

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=9292,
            threaded=False,
            processes=1)
