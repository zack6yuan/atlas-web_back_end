#!/usr/bin/env node
export class Utils {
    constructor() {
        this.calculateNumber = calculateNumber
    }
    function calculateNumber(type, a, b) {
        let new_a = Math.round(a)
        let new_b = Math.round(b)
        if (type === "SUM") {
            return new_a + new_b;
        } else if (type === "SUBTRACT") {
            return new_a - new_b;
        } else if (type === "DIVIDE") {
            if (new_b === 0) {
                return "Error"
            }
            return new_a / new_b;
        }
    }
    
    module.exports = calculateNumber;
}