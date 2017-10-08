#!/usr/bin/env python

import sys
import zmq # pip install pyzmq
import json

# print message using sys
def print(message):
    sys.stdout.write(message + "\n")
    pass

# receive message
def receive_message():
    message = json.loads(rpc.recv())
    try:
        if message['cmd'] == 'rpc':
            print("Python RPC message {}".format(message))
            rpc.send_json({'cmd': 'rpc', 'paylod': '1'})
        elif message['cmd'] == 'exit':
            print("Python RPC message {}".format(message))
            sys.exit(0)
    except KeyboardInterrupt:
        pass
    return

# main function
def main():
    context = zmq.Context()
    rpc = context.socket(zmq.REQ)
    rpc.connect ("tcp://127.0.0.1:8688")
    print("Python RPC conncted to server...")
    rpc.send_json({'cmd': 'conn', 'payload': 'success'})
    
    # recieve message function
    receive_message()
    return

if __name__ == "__main__":
    main()