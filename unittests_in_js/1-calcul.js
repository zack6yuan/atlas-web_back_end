#!/usr/bin/env node
// Calculate number function
function calculateNumber(type, a, b) {
    if (type === "SUM") {
        return Math.round(a) + Math.round(b)
    } else if (type === "SUBTRACT") {
        return Math.round(a) - Math.round(b)
    } else if (type === "DIVIDE") {
        return Math.round(a) / Math.round(b)
    } else if (Math.round(b) === 0) {
        return "Error"
    } else {
        return
    }
}

module.exports = calculateNumber;