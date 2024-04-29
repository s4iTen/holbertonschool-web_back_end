const { calculateNumber } = require('./2-calcul_chai.js');
const { expect } = require('chai');

describe('calculateNumber function using Chai expect', () => {
    describe('First number rounded', () => {
        it('should return the correct sum when the first number is rounded', () => {
            expect(calculateNumber('SUM', 1, 3)).to.equal(4);
            // Add more test cases if needed
        });
    });

    describe('Second number rounded', () => {
        it('should return the correct sum when the second number is rounded', () => {
            expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
            expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
            // Add more test cases if needed
        });
    });

    describe('Both numbers rounded', () => {
        it('should return the correct sum when both numbers are rounded', () => {
            expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
            // Add more test cases if needed
        });
    });
});
