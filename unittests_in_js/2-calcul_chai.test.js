const chai = require('chai')
const {expect} = chai;
const calculateNumber = require('./2-calcul.js')
describe('CalculateNumber', function () {
    it('should return the sum, difference, and quotient of integers', function () {
        expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6)
        expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4)
        expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2)
        expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error")
    });
});