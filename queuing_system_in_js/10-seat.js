const express = require('express')
const app = express()
const port = 1245

let available_seats = 50

const kue = require('kue')
const queue = kue.createQueue()

queue.create('reserve_seat', {
}).save()

function reserveSeat(number) {
    const data = {
        available_seats: number
    };
    return (data);
}

function getCurrentAvailableSeats() {
    return (available_seats);
}