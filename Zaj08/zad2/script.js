'use strict'

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
        chai.assert.equal(cyfry('111'), 3)
    })
    it("litery_sameCyfry", function() {
        chai.assert.equal(litery('111'), 0)
    })
    it("suma_sameCyfry", function() {
        chai.assert.equal(suma('111'), 111)
    })

    it("cyfry_sameLitery", function() {
        chai.assert.equal(cyfry('aa'), 0)
    })
    it("litery_sameLitery", function() {
        chai.assert.equal(litery('aa'), 2)
    })
    it("suma_sameLitery", function() {
        chai.assert.equal(suma('aa'), 111)
    })

    it("cyfry_literyCyfry", function() {
        chai.assert.equal(cyfry('aa11'), 2)
    })
    it("litery_literyCyfry", function() {
        chai.assert.equal(litery('aa11'), 2)
    })
    it("suma_literyCyfry", function() {
        chai.assert.equal(suma('aa11'), 111)
    })

    it("cyfry_cyfryLitery", function() {
        chai.assert.equal(cyfry('11aa'), 2)
    })
    it("litery_cyfryLitery", function() {
        chai.assert.equal(litery('11aa'), 2)
    })
    it("suma_cyfryLitery", function() {
        chai.assert.equal(suma('11aa'), 122)
    })

    it("cyfry_cyfryLitery", function() {
        chai.assert.equal(cyfry(''), 0)
    })
    it("litery_cyfryLitery", function() {
        chai.assert.equal(litery(''), 0)
    })
    it("suma_cyfryLitery", function() {
        chai.assert.equal(suma(''), 122)
    })
})
/* */