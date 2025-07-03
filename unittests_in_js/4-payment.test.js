const sinon = require('sinon')
const Utils = require('./utils.js')

describe('CalculateNumber', function() {
    const stub = sinon.stub(Utils, "calculateNumber")
    const newSpy = sinon.spy(console, "log")

    stub.restore()
    newSpy.restore()
});