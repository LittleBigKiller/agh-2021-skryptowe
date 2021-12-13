var assert = require('assert'); // import w stylu CommonJS
var fs_script = require('../fs');

describe('The checkExists() function', function () {
  it('Returns true for existing file', function () {
    assert.strictEqual(fs_script.checkExists('./Zaj10/fs.js'), true)
  });
  it('Returns true for existing dir', function () {
    assert.strictEqual(fs_script.checkExists('./Zaj10/test'), true)
  });
  it('Returns false for nonexistent dir/file', function () {
    assert.strictEqual(fs_script.checkExists('./Zaj10/no_such_file'), false)
  });
});

describe('The checkIsDir() function', function () {
  it('Returns true for existing dir', function () {
    assert.strictEqual(fs_script.checkIsDir('./Zaj10/test'), true)
  });
  it('Returns false for existing file', function () {
    assert.strictEqual(fs_script.checkIsDir('./Zaj10/fs.js'), false)
  });
  it('Returns false for nonexistent dir/file', function () {
    assert.strictEqual(fs_script.checkIsDir('./Zaj10/no_such_file'), false)
  });
});

describe('The checkIsFile() function', function () {
  it('Returns true for existing file', function () {
    assert.strictEqual(fs_script.checkIsFile('./Zaj10/fs.js'), true)
  });
  it('Returns false for existing dir', function () {
    assert.strictEqual(fs_script.checkIsFile('./Zaj10/test'), false)
  });
  it('Returns false for nonexistent dir/file', function () {
    assert.strictEqual(fs_script.checkIsFile('./Zaj10/no_such_file'), false)
  });
});
