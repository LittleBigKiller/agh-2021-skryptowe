//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var assert = require('assert');
var fs = require('fs');

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('GET /', function () {
  it('respond with html', function (done) {
    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('contain "3" in h1', function (done) {
    function testValue(res) {
      if (!(res.text.match(/(?<=<h1>)[0-9]+(?=<\/h1>)/gm)[0] == 3))
        throw new Error('response doesn\'t match')
    }

    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200)
      .expect(testValue)
      .end(done)
  });
});

describe('Check example.json', function () {
  it('is a json file', function (done) {
    expect('./Zaj11/example.json').to.be.a.jsonFile();
    done()
  });

  it('contains at least one element matching schema', function (done) {
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "+"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "+"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "-"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "-"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "*"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "*"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "/"
    })
    expect('./Zaj11/example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "/"
    })
    done()
  })
})

describe('GET /json/:name (using example.json)', function () {
  it('respond with html', function (done) {
    server
      .get('/json/example.json')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('contain correct value for all operations', function (done) {
    server
      .get('/json/example.json')
      .expect('Content-Type', /html/)
      .expect(200)
      .expect((res) => {
        var match = res.text.match(/(?<=<tr>).*?(?=<\/tr>)/gm)
        for (line of match) {
          var lm = line.match(/(?<=<td>).*?(?=<\/td>)/gm)
          if (lm !== null) {
            assert.equal(eval(lm[0] + lm[1] + lm[2]), lm[3])
          }
        }

      })
      .end(done)
  })
})