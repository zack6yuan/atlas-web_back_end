const sinon = require('sinon')
const Utils = require('./utils.js')
const sendPaymentRequestToApi = require('./3-payment')

const newSpy = sinon.spy(sendPaymentRequestToApi);

const stub = sinon.stub(Utils, 'sendPaymentRequestToApi')