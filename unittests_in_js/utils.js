// utils.js
const Utils = {
    calculateNumber(type, a, b) {
        if (type === 'SUM') {
            return Math.round(a) + Math.round(b);
        }
    }
};

module.exports = Utils;
