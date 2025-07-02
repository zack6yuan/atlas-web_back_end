const assert = require('assert')
const calculateNumber = require('./0-calcul.js')
describe('CalculateNumber', function() {
    it('should return the sum of integer arguments', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
});