#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-04-04
from setuptools import setup, find_packages
from grpc_tools import protoc

# run bdware proto codegen
protoc.main((
    '',
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    './scheduletool/bdware/proto/schedule_service.proto', ))

protoc.main((
    '',
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    './scheduletool/buaacps/proto/entity.proto', ))

protoc.main((
    '',
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    './scheduletool/buaacps/proto/result.proto', ))

setup(
    name='scheduling-tool',
    packages=find_packages(where='.'),
    version='0.0.0',
    description='the scheduling tool for CloudCPS.',
    keywords='scheduling CloudCPS',
    author='barriery',
    url='https://github.com/barrierye/SchedulingTool',
    install_requires=[
        'protobuf>=3.12.2',
        'PyMySQL==0.9.3',
        'sshtunnel==0.1.5',
    ],
)
