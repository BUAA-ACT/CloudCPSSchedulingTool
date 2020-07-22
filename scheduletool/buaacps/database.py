#-*- coding:utf8 -*-
# Copyright (c) 2012 barriery
# Python release: 3.7.0
import pymysql
import json
import sshtunnel
import copy
import datetime

class DatabaseManager(object):
    def __init__(self, remote_ip, remote_usr, remote_pwd, database_usr, database_pwd, database_name):
        self.server = sshtunnel.SSHTunnelForwarder(
                (remote_ip, 22),
                ssh_username=remote_usr,
                ssh_password=remote_pwd,
                remote_bind_address=('localhost', 3306))
        self.server.start()
        self.conn = pymysql.connect(
                user=database_usr,
                password=database_pwd,
                host='127.0.0.1',
                database=database_name,
                port=self.server.local_bind_port)
    def __del__(self):
        self.conn.close()
        self.server.stop()
    def queryNewestItems(self, table, timelabel):
        with self.conn.cursor() as cursor:
            sql_cmd = f"select * from {table} where {timelabel}=" \
                    + f"(select max({timelabel}) from {table})"
            print(sql_cmd)
            cursor.execute(sql_cmd)
            data = cursor.fetchall()
            return data
    def queryItems(self, table, condition=None):
        with self.conn.cursor() as cursor:
            sql_cmd = f"select * from {table}"
            if condition:
                sql_cmd += f" where {condition}"
            print(sql_cmd)
            cursor.execute(sql_cmd)
            data = cursor.fetchall()
            return data
    def in_table(self, table, condition):
        with self.conn.cursor() as cursor:
            sql_cmd = f"select * from {table} where {condition}"
            cursor.execute(sql_cmd)
            data = cursor.fetchone()
            return data is not None
    def insert(self, table, params):
        with self.conn.cursor() as cursor:
            keys = None
            values = None
            for k, v in params.items():
                keys = k if keys is None else "%s, %s"%(keys, k)
                values = "'%s'"%v if values is None else "%s, '%s'"%(values, v)
            sql_cmd = "insert into %s (%s) values (%s)" % (table, keys, values)
            cursor.execute(sql_cmd)
            self.conn.commit()
