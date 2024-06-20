const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
    let consoleLogSpy;

    beforeEach(function() {
        consoleLogSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        consoleLogSpy.restore();
    });

    it('should call sendPaymentRequestToApi with 100 and 20, and log correct message once', function() {
        sendPaymentRequestToApi(100, 20);
        expect(consoleLogSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
        expect(sendPaymentRequestToApi).to.equal(120);
    });

    it('should call sendPaymentRequestToApi with 10 and 10, and log correct message once', function() {
        sendPaymentRequestToApi(10, 10);
        expect(consoleLogSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
        expect(sendPaymentRequestToApi).to.equal(20);
    });
});
