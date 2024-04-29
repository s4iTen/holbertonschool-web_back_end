// 2-calcul_chai.js
const calculateNumber = (type, a, b) => {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    switch (type) {
        case 'SUM':
            return a + b;
        case 'SUBTRACT':
            return a - b;
        case 'DIVIDE':
            return b === 0 ? 'Error' : a / b;
        default:
            throw new Error('Invalid type. Use SUM, SUBTRACT, or DIVIDE.');
    }
};

module.exports = calculateNumber;