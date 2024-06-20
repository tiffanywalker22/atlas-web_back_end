const request = require('request');
const expect = require('chai').expect;
const app = require('./api');

describe('Index page', function() {
    it('Correct status code?', function(done) {
        request('http://localhost:7865/', function (error, response) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('Correct result?', function(done) {
        request('http://localhost:7865/', function (error, response, body) {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });

    it('Other?', function(done) {

        done();
    });
});
