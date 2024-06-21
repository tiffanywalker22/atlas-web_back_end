const request = require('request');
const { expect } = require('chai');
const app = require('./api');

describe('Cart page', () => {
    it('Correct status code when :id is a number?', (done) => {
        request('http://localhost:7865/cart/12', (error, response) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('Correct status code when :id is NOT a number (=> 404)?', (done) => {
        request('http://localhost:7865/cart/hello', (error, response) => {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });

    it('Other?', (done) => {
        done();
    });

    after(() => {
        app.close();
    });
});
