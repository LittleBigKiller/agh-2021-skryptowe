//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8082");

// UNIT test begin
describe('GET /submit?cmds=<file>', function () {
  it('respond with plaintext', function (done) {
    server
      .get('/submit?cmds=del+2345235')
      .expect('Content-Type', /text\/plain/)
      .expect(200, done);
  });
});

describe('GET /submit?cmds=<file>', function () {
  it('respond with \'query failed\' for nonexistent files', function (done) {
    server
      .get('/submit?cmds=del+v')
      .expect('Content-Type', /text\/plain/)
      .expect(200, 'query failed', done);
  });
});

describe('GET /submit?cmds=<file>', function () {
  it('respond with \'query failed\' for chain of operations if one file doesn\'t exist', function (done) {
    server
      .get('/submit?cmds=del+f%0D%0Adel+x%0D%0Adel+z')
      .expect('Content-Type', /text\/plain/)
      .expect(200, 'query failed', done);
  });
});

describe('GET /submit?cmds=<file>', function () {
  it('respond with dir content if succeeds', function (done) {
    server
      .get('/submit?cmds=del+g')
      .expect('Content-Type', /text\/plain/)
      .expect(200, 'deleted file del_me:\n.eslintrc.js\nasync_fs.js\ndokumentacja\nfs.js\nindex.mjs\nlab.js\nmodule.mjs\nnode_modules\npackage-lock.json\npackage.json\nreadme.txt\nscript.js\nserver.js\ntest', done);
  });
});