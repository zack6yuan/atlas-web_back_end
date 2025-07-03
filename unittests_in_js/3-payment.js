const { calculateNumber } = require('./3-payment')
import { Utils } from './utils.js'

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const result = Utils.calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is: ${result}`)
}

module.exports = sendPaymentRequestToApi