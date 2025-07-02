const { calculateNumber } = require('./3-payment')

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const result = calculateNumber(SUM, totalAmount, totalShipping)
    console.log(`The total is: ${result}`)
}

module.exports = sendPaymentRequestToApi