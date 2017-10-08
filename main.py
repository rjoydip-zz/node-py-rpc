#!/usr/bin/env python

import sys
import zmq # pip install pyzmq
import json

# print message using sys
def print(message):
    sys.stdout.write(message)
    return True

context = zmq.Context()
rpc = context.socket(zmq.REQ)
rpc.connect ("tcp://127.0.0.1:8688")

print("Python RPC conncted to server...")

rpc.send_json({'cmd': 'conn', 'payload': 'success'})
message = json.loads(rpc.recv())

print("Py message {}".format(message))

try:
    if message['cmd'] == 'rpc':
        sys.stdout.write("Python RPC message {}".format(message))
        rpc.send_json({'cmd': 'rpc', 'paylod': '1'})
    elif message['cmd'] == 'exit':
        rpc.send_json("Python RPC message {}".format(message))
        sys.exit(0)
except KeyboardInterrupt:
    pass
