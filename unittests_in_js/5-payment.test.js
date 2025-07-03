const chai = require('chai')
const sinon = require('sinon')
const { expect } = chai;
describe('sendPaymentRequestToApi', function() {
    it('should verify the console is logging', function() {
        expect(console.log.calledWith('The total is: 120')).to.be.true;
        expect(console.log.calledOnce).to.be.true;
    })
    it('should verify the console is logging', function() {
        expect(console.log.calledWith('The total is: 20')).to.be.true;
        expect(console.log.calledOnce).to.be.true;
    })
})