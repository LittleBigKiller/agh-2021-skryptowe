//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8080");

// UNIT test begin
describe('GET /submit?fpath=async_fs.js', function () {
  it('respond with "async_fs.js is a file"', function (done) {
    server
      .get('/submit?fpath=async_fs.js')
      .expect('Content-Type', /text\/plain/)
      .expect(200, "async_fs.js is a file", done);
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