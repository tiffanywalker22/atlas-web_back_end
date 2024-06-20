const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
    let calculateNumberStub;
    let consoleLogSpy;

    beforeEach(function() {
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleLogSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        calculateNumberStub.restore();
        consoleLogSpy.restore();
    });

    it('should call sendPaymentRequestToApi with 100 and 20, and log correct message once', function() {
        sendPaymentRequestToApi(100, 20);
        expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(consoleLogSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    });

    it('should call sendPaymentRequestToApi with 10 and 10, and log correct message once', function() {
        sendPaymentRequestToApi(10, 10);
        expect(calculateNumberStub.calledOnceWithExactly('SUM', 10, 10)).to.be.true;
        expect(consoleLogSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    });
});
