const express = require('express') // require the express module
const app = express() // assign to the variable app
const port = 1245 // set the app to run on port 1245

let available_seats = 50 // initialize abailable seats

const kue = require('kue') // require the Kue module
const queue = kue.createQueue() // create a queue with Kue

queue.create('reserve_seat', { // create queue "reserve_seat"
}).save()

function reserveSeat(number) {
    const data = {
        available_seats: number
    };
    return (data); // return the data
}

function getCurrentAvailableSeats() {
    return (available_seats); // retuen the available seats
}