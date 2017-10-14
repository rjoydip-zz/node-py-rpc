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

# connection success payload
rpc.send_json({'cmd': 'conn', 'payload': 'success'})

# print message using sys
def print(message):
    sys.stdout.write(message + "\n")
    return

# send json payload
def __send_json(cmd, payload):
    try:
        rpc.send_json({'cmd': cmd, 'paylod': payload})
        print('Payload send successfully')
    except Exception as e:
        print(str(e))
    return

# send method
def __conn():
    print("__conn working")
    __send_json('conn', 'success')
    return

# send method
def __exit():
    print("exit python process")
    rpc.close()
    sys.exit(0)
    return

# send method
def __send():
    print("__send working")
    __send_json('send', '1')
    return

# main function
@execute
def main():  
    print("Main method start working")
    return

if (__name__ == "__main__"):
    main()