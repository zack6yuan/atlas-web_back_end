const { calculateNumber } = require('./3-payment')
const { Utils } = require('./utils.js')

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const result = Utils.calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is: ${result}`)
}

module.exports = sendPaymentRequestToApi