// 1-calcul.js
export const calculateNumber = (type, a, b) => {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    switch (type) {
        case 'SUM':
            return roundedA + roundedB;
        case 'SUBTRACT':
            return roundedA - roundedB;
        case 'DIVIDE':
            return roundedB === 0 || roundedA === 0 ? 'Error' : roundedA / roundedB;
        default:
            throw new Error('Invalid type. Use SUM, SUBTRACT, or DIVIDE.');
    }
};