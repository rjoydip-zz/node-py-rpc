#!/usr/bin/env python

import sys
import zmq # pip install pyzmq
import json
from decorator import *

TCP_PORT = '8688'
TCP_ADDRESS = 'tcp://127.0.0.1'
TCP_URL = TCP_ADDRESS + ":" + TCP_PORT

# TCP connection stablish
context = zmq.Context()
rpc = context.socket(zmq.REQ)
rpc.connect(TCP_URL)
print("Python RPC conncted with server")

# print message using sys
def print(message):
    sys.stdout.write(str(message) + "\n")
    return

# send json payload
def __send_json(cmd, payload):
    try:
        rpc.send_json({'cmd': cmd, 'paylod': payload})
        print('Python payload send successfully')
    except Exception as e:
        print(e)
    return

# exit process and method method
def _exit():
    print("Exit python process and closing RPC")
    rpc.close()
    sys.exit(0)
    return
    
# send method
def conn():
    print("Python conn working")
    __send_json('conn', 'success')
    return

# send method
def send():
    print("Python send working")
    __send_json('send', '1')
    return
    
@execute
def main():
    return

if (__name__ == "__main__"): 
    try:
        main()
    except KeyboardInterrupt:
        _exit()