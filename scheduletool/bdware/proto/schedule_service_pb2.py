# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schedule_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='schedule_service.proto',
  package='schedule.bdware',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16schedule_service.proto\x12\x0fschedule.bdware\":\n\x08NodeInfo\x12\x0c\n\x04home\x18\x01 \x02(\t\x12\x0f\n\x07storage\x18\x02 \x02(\x02\x12\x0f\n\x07traffic\x18\x03 \x02(\x02\"Z\n\x1bLoadBalancingByNodesRequest\x12(\n\x05nodes\x18\x01 \x03(\x0b\x32\x19.schedule.bdware.NodeInfo\x12\x11\n\tthreshold\x18\x02 \x02(\x02\"0\n\x1cLoadBalancingByNodesResponse\x12\x10\n\x08json_str\x18\x01 \x02(\t2\x88\x01\n\x0fScheduleService\x12u\n\x14LoadBalancingByNodes\x12,.schedule.bdware.LoadBalancingByNodesRequest\x1a-.schedule.bdware.LoadBalancingByNodesResponse\"\x00'
)




_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='schedule.bdware.NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='schedule.bdware.NodeInfo.home', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage', full_name='schedule.bdware.NodeInfo.storage', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traffic', full_name='schedule.bdware.NodeInfo.traffic', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=101,
)


_LOADBALANCINGBYNODESREQUEST = _descriptor.Descriptor(
  name='LoadBalancingByNodesRequest',
  full_name='schedule.bdware.LoadBalancingByNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='schedule.bdware.LoadBalancingByNodesRequest.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='schedule.bdware.LoadBalancingByNodesRequest.threshold', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=193,
)


_LOADBALANCINGBYNODESRESPONSE = _descriptor.Descriptor(
  name='LoadBalancingByNodesResponse',
  full_name='schedule.bdware.LoadBalancingByNodesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_str', full_name='schedule.bdware.LoadBalancingByNodesResponse.json_str', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=243,
)

_LOADBALANCINGBYNODESREQUEST.fields_by_name['nodes'].message_type = _NODEINFO
DESCRIPTOR.message_types_by_name['NodeInfo'] = _NODEINFO
DESCRIPTOR.message_types_by_name['LoadBalancingByNodesRequest'] = _LOADBALANCINGBYNODESREQUEST
DESCRIPTOR.message_types_by_name['LoadBalancingByNodesResponse'] = _LOADBALANCINGBYNODESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEINFO,
  '__module__' : 'schedule_service_pb2'
  # @@protoc_insertion_point(class_scope:schedule.bdware.NodeInfo)
  })
_sym_db.RegisterMessage(NodeInfo)

LoadBalancingByNodesRequest = _reflection.GeneratedProtocolMessageType('LoadBalancingByNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADBALANCINGBYNODESREQUEST,
  '__module__' : 'schedule_service_pb2'
  # @@protoc_insertion_point(class_scope:schedule.bdware.LoadBalancingByNodesRequest)
  })
_sym_db.RegisterMessage(LoadBalancingByNodesRequest)

LoadBalancingByNodesResponse = _reflection.GeneratedProtocolMessageType('LoadBalancingByNodesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOADBALANCINGBYNODESRESPONSE,
  '__module__' : 'schedule_service_pb2'
  # @@protoc_insertion_point(class_scope:schedule.bdware.LoadBalancingByNodesResponse)
  })
_sym_db.RegisterMessage(LoadBalancingByNodesResponse)



_SCHEDULESERVICE = _descriptor.ServiceDescriptor(
  name='ScheduleService',
  full_name='schedule.bdware.ScheduleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=246,
  serialized_end=382,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoadBalancingByNodes',
    full_name='schedule.bdware.ScheduleService.LoadBalancingByNodes',
    index=0,
    containing_service=None,
    input_type=_LOADBALANCINGBYNODESREQUEST,
    output_type=_LOADBALANCINGBYNODESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULESERVICE)

DESCRIPTOR.services_by_name['ScheduleService'] = _SCHEDULESERVICE

# @@protoc_insertion_point(module_scope)
