// Application using the 'Pug' template system
const express = require('express')
const logger = require('morgan')
const fs = require('fs')
var app = express()

const mongoose = require('mongoose')
const { Schema } = mongoose;
mongoose.connect('mongodb://localhost:27017/skryptowe');
const riverSchema = new Schema({
    name: String,
    date: Date,
    value: Number
})
const River = mongoose.model('River', riverSchema);

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {
    res.send(`<form method="GET" action="/submit">
                  <label for="name">Name</label>
                  <input name="name" type="text" required>
                  <br>
                  <label for="date">Date</label>
                  <input name="date" type="date" required>
                  <br>
                  <label for="hval">Value</label>
                  <input name="hval" type="number" required>
                  <br>
                  <input type="submit">
                  <input type="reset">
                </form>`);
});

app.get('/submit', async function (req, res) {
    var url = new URL(req.url, `http://${req.headers.host}`);
    var newRiver = new River({
        name: url.searchParams.get('name'),
        date: url.searchParams.get('date'),
        value: url.searchParams.get('hval')
    });
    await newRiver.save()
    res.send(`<h1>Saved new river with params:</h1><br>name: ${url.searchParams.get('name')}, <br>date: ${url.searchParams.get('date')}, <br>hval: ${url.searchParams.get('hval')}`);
});

app.get('/rivers/:ord(asc|desc)/:rivers(*)', async function (req, res) {
    var rivers = req.params.rivers.split('/')
    
    search_params = '['
    for (river of rivers) {
        search_params += `{ "name": "${river}"}, `
    }
    search_params = search_params.slice(0, -2);
    search_params += ']'

    var json = await River.find( {$or: JSON.parse(search_params)}).sort({ date: req.params.ord }).exec()

    find_params = ''

    find_params += '<table border="1">'
    find_params += '<tr>'
    find_params += '<th>Date</th>'
    find_params += '<th>Name</th>'
    find_params += '<th>Value</th>'
    find_params += '</tr>'

    for (var obj of json) {
        find_params += '<tr>'
        find_params += '<td>'
        find_params += new Date(obj.date).toLocaleString('pl-PL')
        find_params += '</td>'
        find_params += '<td>'
        find_params += obj.name
        find_params += '</td>'
        find_params += '<td>'
        find_params += obj.value
        find_params += '</td>'
        find_params += '</tr>'
    }
    find_params += '</table>'

    res.send(find_params)
});

const PORT = 8080;
// The application is to listen on port number PORT
app.listen(PORT, function () {
    console.log(`The application is available on port ${PORT}`);
});