const assert = require('assert')
const calculateNumber = require('./0-calcul.js')
describe('CalculateNumber', function() {
    it('should return the sum of integers', function() {
        assert.equal(calculateNumber(1, 3), 4);
    });
});