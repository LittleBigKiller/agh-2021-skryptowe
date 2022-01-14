//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var assert = require('assert');
var fs = require('fs');

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

const mongoose = require('mongoose')
const { Schema } = mongoose;
const riverSchema = new Schema({
    name: String,
    date: Date,
    value: Number
})
const River = mongoose.model('River', riverSchema);

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8080");

// UNIT test begin
describe('Zaj11', function () {
    describe('Lab', function () {
        describe('GET /', function () {
            it('respond with html', function (done) {
                server
                    .get('/')
                    .expect('Content-Type', /html/)
                    .expect(200, done);
            });
        });

        describe('GET /rivers/:ord/:rivers', function () {
            it('respond with html', function (done) {
                server
                    .get('/rivers/asc/bsd')
                    .expect('Content-Type', /html/)
                    .expect(200, done);
            });

            it('do not respond to bad params', function (done) {
                server
                    .get('/rivers/asd/bsd')
                    .expect(404, done);
            });

            it('respond to multiple params', function (done) {
                server
                    .get('/rivers/asc/bsd/asd')
                    .expect('Content-Type', /html/)
                    .expect(200, done);
            });
        })
    });
});