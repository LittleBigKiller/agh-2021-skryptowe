'use strict'

var expect = chai.expect;

function sum(x, y) {
    return x + y;
}

describe('The sum() function', function() {
    it('Returns 4 for 2+2', function() {
        expect(sum(2, 2)).to.equal(4);
    });
    it('Returns 0 for -2+2', function() {
        expect(sum(-2, 2)).to.equal(0);
    });
});

var total = 0

function cyfry(napis) {
    var nums = napis.replace(/[^0-9]/g, '')
    nums = nums.split('')
    nums.map(function(n) {
        return parseInt(n)
    })

    if (nums.length == 0)
        return 0

    var sum = nums.reduce(function(total, num) {
        return parseInt(total) + parseInt(num)
    })

    if (isNaN(sum)) {
        return 0
    } else {
        return sum
    }
}

function litery(napis) {
    return (napis.match(/\p{L}/gu) || []).length;
}

function suma(napis) {
    var nn = parseInt(napis)
    if (!isNaN(nn))
        total += nn
    return total
}

/* */
var data = ''
while (true) {
    data = window.prompt('Podaj dane')

    if (data == null)
        break

    console.log('\t' + cyfry(data) + '\t' + litery(data) + '\t' + suma(data))
}
/* */
describe("funkcje script.js", function() {
    total = 0

    it("cyfry_sameCyfry", function() {
        expect(cyfry('111')).to.equal(3)
    })
    it("litery_sameCyfry", function() {
        expect(litery('111')).to.equal(0)
    })
    it("suma_sameCyfry", function() {
        expect(suma('111')).to.equal(111)
    })

    it("cyfry_sameLitery", function() {
        expect(cyfry('aa')).to.equal(0)
    })
    it("litery_sameLitery", function() {
        expect(litery('aa')).to.equal(2)
    })
    it("suma_sameLitery", function() {
        expect(suma('aa')).to.equal(111)
    })

    it("cyfry_literyCyfry", function() {
        expect(cyfry('aa11')).to.equal(2)
    })
    it("litery_literyCyfry", function() {
        expect(litery('aa11')).to.equal(2)
    })
    it("suma_literyCyfry", function() {
        expect(suma('aa11')).to.equal(111)
    })

    it("cyfry_cyfryLitery", function() {
        expect(cyfry('11aa')).to.equal(2)
    })
    it("litery_cyfryLitery", function() {
        expect(litery('11aa')).to.equal(2)
    })
    it("suma_cyfryLitery", function() {
        expect(suma('11aa')).to.equal(122)
    })

    it("cyfry_pustyNapis", function() {
        expect(cyfry('')).to.equal(0)
    })
    it("litery_pustyNapis", function() {
        expect(litery('')).to.equal(0)
    })
    it("suma_pustyNapis", function() {
        expect(suma('')).to.equal(122)
    })
})
/* */