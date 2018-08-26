# -*- coding: utf-8 -*-
from .client import LineClient
from types import *

import os, sys, threading,traceback,subprocess

class LinePoll(object):
    OpInterrupt = {}
    client = None

    def __init__(self, client):
        if type(client) is not LineClient:
            raise Exception("You need to set LineClient instance to initialize LinePoll")
        self.client = client
    
    def fetchOperation(self, revision, count=10):
        return self.client.poll.fetchOperations(revision, count)

    def addOpInterruptWithDict(self, OpInterruptDict):
        self.OpInterrupt.update(OpInterruptDict)

    def addOpInterrupt(self, OperationType, DisposeFunc):
        self.OpInterrupt[OperationType] = DisposeFunc
        
    def execute(self, op, threading=False):
        try:
            self.OpInterrupt[op.type](op)
        except Exception as e:
            h = traceback.format_exc()
            with open("e","a") as error:
                error.write("\n{}".format(h))
            self.client.log(str(h))
    
    def trace(self):
        try:
            operations = self.fetchOperation(self.client.revision)
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            return
        
        for op in operations:
            if op.type in self.OpInterrupt.keys():
                threading.Thread(target=self.execute,args=(op,)).start()
            self.client.revision = max(op.revision, self.client.revision)