const chai = require('chai')
const { expect } = chai;
const getPaymentTokenFromAPI = require('./6-payment_token');
describe('PaymentToken', function() {
    it('should ensure the result is true', function() {
        expect(getPaymentTokenFromAPI).to.be.true;
    });
});