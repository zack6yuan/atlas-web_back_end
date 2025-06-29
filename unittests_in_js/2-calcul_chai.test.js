const assert = require('assert')
const expect = require('expect')
const chai = require('chai')
const calculateNumber = require('./1-calcul.js')
describe('CalculateNumber', function () {
    it('should return the sum, difference, and quotient of integers', function () {
        expect(calculateNumber("SUM", 1.4, 1.5)).toEqual(6)
        expect(calculateNumber("SUBTRACT", 1.4, 4.5)).toEqual(-4)
        expect(calculateNumber("DIVIDE", 1.4, 4.5)).toEqual(0.2)
        expect(calculateNumber("DIVIDE", 1.4, 0)).toEqual("Error")
    });
});