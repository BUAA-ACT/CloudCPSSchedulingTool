# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scheduletool/buaacps/proto/entity.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scheduletool/buaacps/proto/entity.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'scheduletool/buaacps/proto/entity.proto\"\x8f\x01\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1f\n\ncloudlayer\x18\x02 \x02(\x0b\x32\x0b.CloudLayer\x12#\n\x0cnetworklayer\x18\x03 \x02(\x0b\x32\r.NetworkLayer\x12\x1b\n\x08\x65ndlayer\x18\x04 \x02(\x0b\x32\t.EndLayer\x12\x14\n\x05links\x18\x05 \x02(\x0b\x32\x05.Link\"&\n\x04Link\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\x0e\n\x06target\x18\x02 \x02(\t\".\n\nCloudLayer\x12 \n\x0b\x64\x61tacenters\x18\x02 \x03(\x0b\x32\x0b.Datacenter\"X\n\nDatacenter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1e\n\ncloudnodes\x18\x04 \x03(\x0b\x32\n.CloudNode\"\x83\x01\n\tCloudNode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x02(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\x01\x12\x0e\n\x06memory\x18\x05 \x01(\x01\x12\r\n\x05store\x18\x06 \x01(\x01\x12\x1e\n\ncontainers\x18\x07 \x03(\x0b\x32\n.Container\"Q\n\tContainer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x63pu\x18\x02 \x02(\x01\x12\x0e\n\x06memory\x18\x03 \x02(\x01\x12\r\n\x05store\x18\x04 \x02(\x01\x12\n\n\x02id\x18\x05 \x02(\t\"L\n\x0cNetworkLayer\x12\x1a\n\x08netnodes\x18\x01 \x03(\x0b\x32\x08.NetNode\x12 \n\x0b\x65\x64geservers\x18\x02 \x03(\x0b\x32\x0b.EdgeServer\"\x81\x01\n\x07NetNode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x02(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\x01\x12\x0e\n\x06memory\x18\x05 \x01(\x01\x12\r\n\x05store\x18\x06 \x01(\x01\x12\x1e\n\ncontainers\x18\x07 \x03(\x0b\x32\n.Container\"\x84\x01\n\nEdgeServer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x02(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\x01\x12\x0e\n\x06memory\x18\x05 \x01(\x01\x12\r\n\x05store\x18\x06 \x01(\x01\x12\x1e\n\ncontainers\x18\x07 \x03(\x0b\x32\n.Container\" \n\x08\x45ndLayer\x12\x14\n\x05rooms\x18\x01 \x03(\x0b\x32\x05.Room\"~\n\x04Room\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x02(\t\x12\x18\n\x07\x64\x65vices\x18\x03 \x03(\x0b\x32\x07.Device\x12\x18\n\x07workers\x18\x04 \x03(\x0b\x32\x07.Worker\x12\"\n\x0c\x61pplications\x18\x05 \x03(\x0b\x32\x0c.Application\"\"\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\t\"\"\n\x06Worker\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\t\"\'\n\x0b\x41pplication\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\t'
)




_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Entity.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cloudlayer', full_name='Entity.cloudlayer', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='networklayer', full_name='Entity.networklayer', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endlayer', full_name='Entity.endlayer', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='links', full_name='Entity.links', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=44,
  serialized_end=187,
)


_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='Link.source', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='Link.target', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=189,
  serialized_end=227,
)


_CLOUDLAYER = _descriptor.Descriptor(
  name='CloudLayer',
  full_name='CloudLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datacenters', full_name='CloudLayer.datacenters', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=229,
  serialized_end=275,
)


_DATACENTER = _descriptor.Descriptor(
  name='Datacenter',
  full_name='Datacenter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Datacenter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='Datacenter.location', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Datacenter.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cloudnodes', full_name='Datacenter.cloudnodes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=277,
  serialized_end=365,
)


_CLOUDNODE = _descriptor.Descriptor(
  name='CloudNode',
  full_name='CloudNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CloudNode.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='CloudNode.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='CloudNode.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='CloudNode.cpu', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='CloudNode.memory', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store', full_name='CloudNode.store', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='containers', full_name='CloudNode.containers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=368,
  serialized_end=499,
)


_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Container.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='Container.cpu', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='Container.memory', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store', full_name='Container.store', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Container.id', index=4,
      number=5, type=9, cpp_type=9, label=2,
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
  serialized_start=501,
  serialized_end=582,
)


_NETWORKLAYER = _descriptor.Descriptor(
  name='NetworkLayer',
  full_name='NetworkLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='netnodes', full_name='NetworkLayer.netnodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edgeservers', full_name='NetworkLayer.edgeservers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=584,
  serialized_end=660,
)


_NETNODE = _descriptor.Descriptor(
  name='NetNode',
  full_name='NetNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='NetNode.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='NetNode.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='NetNode.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='NetNode.cpu', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='NetNode.memory', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store', full_name='NetNode.store', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='containers', full_name='NetNode.containers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=663,
  serialized_end=792,
)


_EDGESERVER = _descriptor.Descriptor(
  name='EdgeServer',
  full_name='EdgeServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='EdgeServer.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='EdgeServer.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='EdgeServer.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='EdgeServer.cpu', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='EdgeServer.memory', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store', full_name='EdgeServer.store', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='containers', full_name='EdgeServer.containers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=795,
  serialized_end=927,
)


_ENDLAYER = _descriptor.Descriptor(
  name='EndLayer',
  full_name='EndLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rooms', full_name='EndLayer.rooms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=929,
  serialized_end=961,
)


_ROOM = _descriptor.Descriptor(
  name='Room',
  full_name='Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Room.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='Room.location', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='devices', full_name='Room.devices', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workers', full_name='Room.workers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='applications', full_name='Room.applications', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=963,
  serialized_end=1089,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Device.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Device.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=1091,
  serialized_end=1125,
)


_WORKER = _descriptor.Descriptor(
  name='Worker',
  full_name='Worker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Worker.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Worker.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=1127,
  serialized_end=1161,
)


_APPLICATION = _descriptor.Descriptor(
  name='Application',
  full_name='Application',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Application.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Application.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=1163,
  serialized_end=1202,
)

_ENTITY.fields_by_name['cloudlayer'].message_type = _CLOUDLAYER
_ENTITY.fields_by_name['networklayer'].message_type = _NETWORKLAYER
_ENTITY.fields_by_name['endlayer'].message_type = _ENDLAYER
_ENTITY.fields_by_name['links'].message_type = _LINK
_CLOUDLAYER.fields_by_name['datacenters'].message_type = _DATACENTER
_DATACENTER.fields_by_name['cloudnodes'].message_type = _CLOUDNODE
_CLOUDNODE.fields_by_name['containers'].message_type = _CONTAINER
_NETWORKLAYER.fields_by_name['netnodes'].message_type = _NETNODE
_NETWORKLAYER.fields_by_name['edgeservers'].message_type = _EDGESERVER
_NETNODE.fields_by_name['containers'].message_type = _CONTAINER
_EDGESERVER.fields_by_name['containers'].message_type = _CONTAINER
_ENDLAYER.fields_by_name['rooms'].message_type = _ROOM
_ROOM.fields_by_name['devices'].message_type = _DEVICE
_ROOM.fields_by_name['workers'].message_type = _WORKER
_ROOM.fields_by_name['applications'].message_type = _APPLICATION
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Link'] = _LINK
DESCRIPTOR.message_types_by_name['CloudLayer'] = _CLOUDLAYER
DESCRIPTOR.message_types_by_name['Datacenter'] = _DATACENTER
DESCRIPTOR.message_types_by_name['CloudNode'] = _CLOUDNODE
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
DESCRIPTOR.message_types_by_name['NetworkLayer'] = _NETWORKLAYER
DESCRIPTOR.message_types_by_name['NetNode'] = _NETNODE
DESCRIPTOR.message_types_by_name['EdgeServer'] = _EDGESERVER
DESCRIPTOR.message_types_by_name['EndLayer'] = _ENDLAYER
DESCRIPTOR.message_types_by_name['Room'] = _ROOM
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['Worker'] = _WORKER
DESCRIPTOR.message_types_by_name['Application'] = _APPLICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Entity)
  })
_sym_db.RegisterMessage(Entity)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
  'DESCRIPTOR' : _LINK,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Link)
  })
_sym_db.RegisterMessage(Link)

CloudLayer = _reflection.GeneratedProtocolMessageType('CloudLayer', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDLAYER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:CloudLayer)
  })
_sym_db.RegisterMessage(CloudLayer)

Datacenter = _reflection.GeneratedProtocolMessageType('Datacenter', (_message.Message,), {
  'DESCRIPTOR' : _DATACENTER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Datacenter)
  })
_sym_db.RegisterMessage(Datacenter)

CloudNode = _reflection.GeneratedProtocolMessageType('CloudNode', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDNODE,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:CloudNode)
  })
_sym_db.RegisterMessage(CloudNode)

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Container)
  })
_sym_db.RegisterMessage(Container)

NetworkLayer = _reflection.GeneratedProtocolMessageType('NetworkLayer', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKLAYER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:NetworkLayer)
  })
_sym_db.RegisterMessage(NetworkLayer)

NetNode = _reflection.GeneratedProtocolMessageType('NetNode', (_message.Message,), {
  'DESCRIPTOR' : _NETNODE,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:NetNode)
  })
_sym_db.RegisterMessage(NetNode)

EdgeServer = _reflection.GeneratedProtocolMessageType('EdgeServer', (_message.Message,), {
  'DESCRIPTOR' : _EDGESERVER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:EdgeServer)
  })
_sym_db.RegisterMessage(EdgeServer)

EndLayer = _reflection.GeneratedProtocolMessageType('EndLayer', (_message.Message,), {
  'DESCRIPTOR' : _ENDLAYER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:EndLayer)
  })
_sym_db.RegisterMessage(EndLayer)

Room = _reflection.GeneratedProtocolMessageType('Room', (_message.Message,), {
  'DESCRIPTOR' : _ROOM,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Room)
  })
_sym_db.RegisterMessage(Room)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Device)
  })
_sym_db.RegisterMessage(Device)

Worker = _reflection.GeneratedProtocolMessageType('Worker', (_message.Message,), {
  'DESCRIPTOR' : _WORKER,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Worker)
  })
_sym_db.RegisterMessage(Worker)

Application = _reflection.GeneratedProtocolMessageType('Application', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATION,
  '__module__' : 'scheduletool.buaacps.proto.entity_pb2'
  # @@protoc_insertion_point(class_scope:Application)
  })
_sym_db.RegisterMessage(Application)


# @@protoc_insertion_point(module_scope)
