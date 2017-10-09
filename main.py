#!/usr/bin/env python

import sys
import zmq # pip install pyzmq
import json

# print message using sys
def print(message):
    sys.stdout.write(message + "\n")
    pass
    
context = zmq.Context()
rpc = context.socket(zmq.REQ)
rpc.connect("tcp://127.0.0.1:8688")
print("Python RPC conncted with server")
    
rpc.send_json({'cmd': 'conn', 'payload': 'success'})
message = json.loads(rpc.recv())

if message['cmd'] == 'send':
    rpc.send_json({'cmd': 'send', 'paylod': '1'})
elif message['cmd'] == 'exit':
    sys.exit(0)