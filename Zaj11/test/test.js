//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var assert = require('assert');
var fs = require('fs');

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

const mongoose = require('mongoose')
const { Schema } = mongoose;
mongoose.connect('mongodb://localhost:27017/skryptowe');
const opSchema = new Schema({
  x: Number,
  y: Number,
  op: String
})
const Op = mongoose.model('Op', opSchema);

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('Zaj11', function () {
  describe('Zad1', function () {
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
  });

  describe('Zad2', function () {
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
  });

  describe('Zad3', function () {

    describe('GET /calculate/:operation/:x/:y (using example.json)', function () {
      it('respond with html', function (done) {
        server
          .get('/calculate/+/1/1')
          .expect('Content-Type', /html/)
          .expect(200, done);
      });

      it('respond correct string in h1', function (done) {
        function testValue(res) {
          console.log(res.text.match(/(?<=<h1>).*?(?=<\/h1>)/gm))
          if (!(res.text.match(/(?<=<h1>).*?(?=<\/h1>)/gm)[0] == '2 + 2 = 4'))
            throw new Error('response doesn\'t match')
        }

        server
          .get('/calculate/+/2/2')
          .expect('Content-Type', /html/)
          .expect(200)
          .expect(testValue)
          .end(done)
      });

      it('check for invalid operations', function (done) {
        server
          .get('/calculate/x/1/1')
          .expect('Content-Type', /html/)
          .expect(400)
          .end(done)
      })

      it('save valid operation to database', function (done) {
        var x = getRandomInt(65535)
        var y = getRandomInt(65535)
        server
          .get('/calculate/-/' + x + '/' + y)
          .expect('Content-Type', /html/)
          .expect(200)
          .expect(async (res) => {
            var json = await Op.find({ x: x, y: y, op: '-' });

            console.log(json.length)

            expect(json.length).to.be.greaterThanOrEqual(1)
          })
          .end(done)
      })
    })

    describe('GET /results', function () {
      it('respond with html', function (done) {
        server
          .get('/results')
          .expect('Content-Type', /html/)
          .expect(200, done);
      });

      it('contain correct value for all operations', function (done) {
        server
          .get('/results')
          .expect('Content-Type', /html/)
          .expect(200)
          .expect(async (res) => {
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
  });
});