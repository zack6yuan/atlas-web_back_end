const assert = require('assert')
const calculateNumber = require('./0-calcul.js')
describe('CalculateNumber', function() {
    it('should return the sum of two arguments', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });
    it('should return two added arguments and round up', function() {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
    it('should return the sum of two arguments', function() {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
    it ('should return two added arguments and round down', function() {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    })
});