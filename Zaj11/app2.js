// Application using the 'Pug' template system
const express = require('express')
const logger = require('morgan')
const fs = require('fs')
var app = express()
var x = 1
var y = 2

const mongoose = require('mongoose')
const { Schema } = mongoose;
mongoose.connect('mongodb://localhost:27017/skryptowe');
const opSchema = new Schema({
    x: Number,
    y: Number,
    op: String
})
const Op = mongoose.model('Op', opSchema);

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

app.get('/calculate/:operation/:x/:y', async function (req, res) {
    if (!["+", "-", "*", "/"].includes(req.params.operation)) {
        res.status(400).send("No such operation")
    }
    else {

        var newOp = new Op({ x: req.params.x, y: req.params.y, op: req.params.operation });
        await newOp.save()

        disp_str = '' + req.params.x + ' ' + req.params.operation + ' ' + req.params.y
        res.render('index', { sum: disp_str + ' = ' + eval(disp_str) });
    }
});

app.get('/results', async function (req, res) {
    var json = await Op.find();

    res.render('json', { json: json });
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});