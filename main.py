#!/usr/bin/env python

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect ("tcp://127.0.0.1:8688")
print("RPC conncted to server...")
socket.send_string("Hello")
message = socket.recv()
print("Received message: %s" % message)