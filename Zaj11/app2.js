// Application using the 'Pug' template system
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

// Configuring the application
app.set('views', __dirname + '/views'); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');          // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {
    res.render('index', { sum: sum(x, y) });
});

app.get('/json/:name', function (req, res) {
    var json = JSON.parse(readFile(req.params.name))

    res.render('json', { json: json });
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});