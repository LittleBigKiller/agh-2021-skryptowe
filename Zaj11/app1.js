// No use of any template system
const express = require('express')
const logger = require('morgan')
const fs = require('fs')
var app = express()
var x = 1
var y = 2

function checkExists(fpath) {
    try {
        if (fs.existsSync(fpath)) {
            return true
        }
        return false
    }
    catch (err) {
        return false
    }
}

function checkIsFile(fpath) {
    if (checkExists(fpath)) {
        if (fs.statSync(fpath).isFile()) {
            return true
        } else {
            return false
        }
    } else {
        return false
    }
}

function readFile(fpath) {
    if (checkIsFile(fpath)) {
        return fs.readFileSync(fpath, { encoding: 'utf8' })
    }
    else {
        return null
    }
}

function sum(x, y) {
    return x + y
}

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {     // The first route
    res.send('<h1>' + sum(x, y) + '</h1>'); // Send a response to the browser
});

app.get('/json/:name', function (req, res) {
    var json = JSON.parse(readFile(req.params.name))

    res_str = '<table border="1">'
    res_str += '<tr>'
    res_str += '<th>x</th>'
    res_str += '<th>Operation</th>'
    res_str += '<th>y</th>'
    res_str += '<th>Result</th>'
    res_str += '</tr>'

    for (var obj of json) {
        res_str += '<tr>'
        res_str += '<td>'
        res_str += obj.x
        res_str += '</td>'
        res_str += '<td>'
        res_str += obj.op
        res_str += '</td>'
        res_str += '<td>'
        res_str += obj.y
        res_str += '</td>'
        res_str += '<td>'
        res_str += eval('' + obj.x + obj.op + obj.y)
        res_str += '</td>'
        res_str += '</tr>'
    }
    res_str += '</table>'

    res.send(res_str);
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});