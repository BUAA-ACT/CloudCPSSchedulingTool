#-*- coding:utf8 -*-
# Copyright (c) 2020 barriery
# Python release: 3.7.0
# Create time: 2020-07-15
import execjs
import json
import requests
from bdcaller import BDCaller

class SM2Executor(object):
    def __init__(self, publicKey, privateKey):
        self.publicKey_ = publicKey
        self.privateKey_ = privateKey

    def sign(self, content, privateKey=None):
        pass

    def verify(self, content, signature, publicKey=None):
        pass

class PySM2Executor(SM2Executor):
    def __init__(self, publicKey, privateKey):
        super(PySM2Executor, self).__init__(publicKey, privateKey)
        from gmssl import sm2
        self.sm2_crypt_ = sm2.CryptSM2(public_key=publicKey, private_key=privateKey)

    def sign(self, content, privateKey=None):
        if privateKey is None:
            privateKey = self.privateKey_
        elif privateKey != self.privateKey_:
            raise Exception("illegal privateKey")
        from gmssl import func
        random_hex_str = func.random_hex(self.sm2_crypt_.para_len)
        if not isinstance(content, bytes):
            content = bytes(content, encoding="utf8")
        sign = self.sm2_crypt_.sign(content, random_hex_str)
        return sign

    def verify(self, content, signature, publicKey=None):
        if publicKey is None:
            publicKey = self.publicKey_
        elif publicKey != self.publicKey_:
            raise Exception("illegal publicKey")
        if not isinstance(content, bytes):
            content = bytes(content, encoding="utf8")
        return self.sm2_crypt_.verify(signature, content)

class JsSM2Executor(SM2Executor):
    def __init__(self, publicKey, privateKey):
        super(JsSM2Executor, self).__init__(publicKey, privateKey)
        js_code = """
            const sm2 = require('sm-crypto').sm2

            function sign(msg, privateKey) {
                let sigValueHex = sm2.doSignature(msg, privateKey)
                return sigValueHex;
            }

            function verify(msg, signature, publicKey) {
                let verifyResult = sm2.doVerifySignature(msg, signature, publicKey)
                return verifyResult
            }
        """
        self.js_ctx_ = execjs.compile(js_code)

    def sign(self, content, privateKey=None):
        if privateKey is None:
            privateKey = self.privateKey_

        return self.js_ctx_.call("sign", content, privateKey)

    def verify(self, content, signature, publicKey=None):
        if publicKey is None:
            publicKey = self.publicKey_

        return self.js_ctx_.call("verify", content, signature, publicKey)

class JavaSM2Executor(SM2Executor):
    def __init__(self, contract_url, publicKey, privateKey):
        super(JavaSM2Executor, self).__init__(publicKey, privateKey)
        self.caller_ = BDCaller(contract_url)

    def generateKeyPair(self):
        params = {
            "action": "executeContract",
            "contractID": "SM2Example",
            "operation": "generateKeyPair",
            "arg": "",
        }

        result = self.caller_.callContract(params)
        
        self.publicKey_ = result["publicKey"]
        self.privateKey_ = result["privateKey"]

    def getPublicKey(self):
        return self.publicKey_

    def getPrivateKey(self):
        return self.privateKey_

    def sign(self, content, privateKey=None):
        if privateKey != self.privateKey_:
            raise Exception("illegal privateKey")

        arg = {
            "content": content,
            "publicKey": self.publicKey_,
            "privateKey": self.privateKey_,
        }
        params = {
            "action": "executeContract",
            "contractID": "SM2Example",
            "operation": "sign",
            "arg": json.dumps(arg),
        }
        
        result = self.caller_.callContract(params)

        signature = result["signature"]
        return signature

    def verify(self, content, signature, publicKey=None):
        if publicKey != self.publicKey_:
            raise Exception("illegal publicKey")

        arg = {
            "content": content,
            "signature": signature,
            "publicKey": self.publicKey_,
        }
        params = {
            "action": "executeContract",
            "contractID": "SM2Example",
            "operation": "verify",
            "arg": json.dumps(arg),
        }

        result = self.caller_.callContract(params)
        return result["result"]
