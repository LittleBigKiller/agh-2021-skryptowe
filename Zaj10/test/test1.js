var assert = require('assert'); // import w stylu CommonJS

describe('The sum() method', function () {
  it('Returns 4 for 2+2', function () {
    // brudny hack, żeby zaimportować "asynchronicznie" moduł ES6 w skrypcie CommonJS
    // niestety mocha-sidebar nie wspiera ES6,
    // a babela nie mieliśmy ustawiać, to jest brudny hack
    import('../module.mjs').then(module => {
      var op = new module.Operation(2, 2);
      assert.strictEqual(op.sum(), 4)
    });
  });
  it('Returns 0 for -2+2', function () {
    // brudny hack, żeby zaimportować "asynchronicznie" moduł ES6 w skrypcie CommonJS
    // niestety mocha-sidebar nie wspiera ES6,
    // a babela nie mieliśmy ustawiać, to jest brudny hack
    import('../module.mjs').then(module => {
      var op = new module.Operation(-2, 2);
      assert.strictEqual(op.sum(), 0)
    });
  });
});
