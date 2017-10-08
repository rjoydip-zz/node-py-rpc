#!/usr/bin/env python

import sys
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect ("tcp://127.0.0.1:8688")
print("Python RPC conncted to server...")

socket.send_json({'cmd': 'conn', 'payload': 'success'})
message = json.loads(socket.recv())

print("Py message {}".format(message))

try:
    if message['cmd'] == 'rpc':
        print("Python RPC message {}".format(message))
        socket.send_json({'cmd': 'rpc', 'paylod': '1'})
    elif message['cmd'] == 'exit':
        print("Python RPC message {}".format(message))
        sys.exit(0)
except KeyboardInterrupt:
    pass
