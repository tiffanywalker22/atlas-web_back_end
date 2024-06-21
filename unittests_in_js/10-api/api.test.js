const request = require('request');
const { expect } = require('chai');

describe('Login endpoint', () => {
    it('should return welcome message with username', (done) => {
        request.post('http://localhost:7865/login', { json: { userName: 'Betty' } }, (error, response, body) => {
            expect(body).to.equal('Welcome Betty');
            done();
        });
    });
});

describe('Available payments endpoint', () => {
    it('should return payment methods object', (done) => {
        request('http://localhost:7865/available_payments', (error, response, body) => {
            expect(JSON.parse(body)).to.deep.equal({
                payment_methods: {
                    credit_cards: true,
                    paypal: false
                }
            });
            done();
        });
    });
});

after(() => {
    app.close();
});
