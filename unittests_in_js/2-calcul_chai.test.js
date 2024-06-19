// 2-calcul_chai.test.js
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function() {
    describe('SUM', function() {
        it('should return 6 when inputs are 1.4 and 4.5', function() {
            expect.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });
    });

    describe('SUBTRACT', function() {
        it('should return -4 when inputs are 1.4 and 4.5', function() {
            expect.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        });
    });

    describe('DIVIDE', function() {
        it('should return 0.2 when inputs are 1.4 and 4.5', function() {
            expect.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        });

        it('should return Error when second input rounds to 0', function() {
            expect.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
            expect.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
        });
    });
});
