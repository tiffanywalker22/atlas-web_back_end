// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
    it('should return 4 when inputs are 1 and 3', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return 5 when inputs are 1 and 3.7', function() {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('should return 5 when inputs are 1.2 and 3.7', function() {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 6 when inputs are 1.5 and 3.7', function() {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should return 0 when inputs are 0 and 0', function() {
        assert.strictEqual(calculateNumber(0, 0), 0);
    });

    it('should return 4 when second number is rounded and inputs are 1 and 3.2', function() {
        assert.strictEqual(calculateNumber(1, 3.2), 4);
    });

    it('should return 6 when both numbers are rounded and inputs are 1.234 and 5.678', function() {
        assert.strictEqual(calculateNumber(1.234, 5.678), 6);
    });

    it('should return -2 when second number is rounded and inputs are 1 and -2.5', function() {
        assert.strictEqual(calculateNumber(1, -2.5), -2);
    });
});