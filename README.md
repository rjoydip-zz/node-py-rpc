# node-py-rpc

> Node.js and python communication using Remote Procedure Call (RPC)

## Locally install

```sh
$ git clone https://github.com/Rjoydip/node-py-rpc.git
$ cd node-py-rpc
$ npm install
$ pip install pyzmq
$ npm start
```

## How it works

* Run node server.
* Node server will run on `localhost:3000`.
* TCP connection will be stablished and this connection will communicate with python on `tcp://127.0.0.1:8688`.
* Hit the `/send` route and it will run python command using `spawn`.

***Note***

> Make sure `pyzmq` installed.

***ISSUE***

> Right now python code communicate once first time when route will be called. From 2nd time onwards it will not execute.