var express = require('express');
var path = require('path');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var path = require('path');
var spawn = require('child_process').spawn;

var zmq = require('zeromq')
var rpc = zmq.socket('rep')

var app = express();

// view engine setup
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: false
}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

function openPyTerminal(method = 'conn', paylaod = null) {
  var dataString = '';
  var args_arr = method && paylaod ? [`./main.py`, method] : ['./main.py'];

  var py = spawn('python', args_arr , {
    env: Object.create(process.env)
  });

  py.stdout.on('data', function (data) {
    process.stdout.write(data.toString());
  });
}

rpc.bind('tcp://127.0.0.1:8688', function (err) {
  console.log('Node RPC running on 8688');
  if (err) console.log(err);
  else openPyTerminal();
});

rpc.on('message', function (payload) {
  var paylaod = JSON.parse(payload.toString());
  console.log("Python payload", paylaod);
});

app.get('/', function (req, res) {
  return res.status(200).send({
    message: "Welcome to node-py-rpc"
  });
});

app.get('/send', function (req, res) {
  openPyTerminal('send', '1');
  rpc.on('message', function (payload) {
    console.log("Node recieve send payload", payload);
    var paylaod = new Buffer(payload).toString('ascii');
    return res.status(200).send({
      payload
    });
  });
});

process.on('exit', (code) => {
  rpc.send(
    JSON.stringify({
      'cmd': 'exit',
      'payload': '-1'
    })
  );
  rpc.close();
  console.log("Node server and rpc connection closes with exit code" + code);
});

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.send({
    err
  });
});

module.exports = app;