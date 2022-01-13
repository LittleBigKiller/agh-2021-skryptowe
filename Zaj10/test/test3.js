//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8080");

// UNIT test begin
describe('Zaj10', function () {
  describe('Zad3', function () {
    describe('GET /submit?fpath=readme.txt', function () {
      it('respond with contents of readme.txt', function (done) {
        server
          .get('/submit?fpath=readme.txt')
          .expect('Content-Type', /text\/plain/)
          .expect(200, "test4me", done);
      });
    });

    describe('GET /submit?fpath=test', function () {
      it('respond with "test is a directory"', function (done) {
        server
          .get('/submit?fpath=test')
          .expect('Content-Type', /text\/plain/)
          .expect(200, "test is a directory", done);
      });
    });

    describe('GET /submit?fpath=no_such_file', function () {
      it('respond with "No such file no_such_file"', function (done) {
        server
          .get('/submit?fpath=no_such_file')
          .expect('Content-Type', /text\/plain/)
          .expect(200, "No such file no_such_file", done);
      });
    });
  });
});