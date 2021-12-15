var assert = require('assert'); // import w stylu CommonJS
var fs_script = require('../fs');

describe('The checkExists() function', function () {
  it('Returns true for existing file', function () {
    assert.strictEqual(fs_script.checkExists('./Zaj10/readme.txt'), true)
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
    assert.strictEqual(fs_script.checkIsDir('./Zaj10/readme.txt'), false)
  });
  it('Returns false for nonexistent dir/file', function () {
    assert.strictEqual(fs_script.checkIsDir('./Zaj10/no_such_file'), false)
  });
});

describe('The checkIsFile() function', function () {
  it('Returns true for existing file', function () {
    assert.strictEqual(fs_script.checkIsFile('./Zaj10/readme.txt'), true)
  });
  it('Returns false for existing dir', function () {
    assert.strictEqual(fs_script.checkIsFile('./Zaj10/test'), false)
  });
  it('Returns false for nonexistent dir/file', function () {
    assert.strictEqual(fs_script.checkIsFile('./Zaj10/no_such_file'), false)
  });
});

describe('The readFile() function', function () {
  it('Returns file contents for existing file', function () {
    assert.strictEqual(fs_script.readFile('./Zaj10/readme.txt'), 'test4me')
  });
  it('Returns null for existing dir', function () {
    assert.strictEqual(fs_script.readFile('./Zaj10/test'), null)
  });
  it('Returns null for nonexistent dir/file', function () {
    assert.strictEqual(fs_script.readFile('./Zaj10/no_such_file'), null)
  });
});
