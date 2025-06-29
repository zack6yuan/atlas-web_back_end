const assert = require('assert')
const calculateNumber = require('./1-calcul.js')
describe('CalculateNumber', function() {
    it('should return the sum, difference, and quotient of integers', function() {
        assert.equal(calculateNumber("SUM", (1.4, 4.5), 6));
        assert.equal(calculateNumber("SUBTRACT", (1.4, 4.5), -4));
        assert.equal(calculateNumber(("DIVIDE", 1.4, 4.5), 0.2));
        assert.equal(calculateNumber(("DIVIDE", 1.4, 0), "'Error'"));
    });
});