const kue = require('kue') // require the Kue module
const queue = kue.createQueue() // create a queue with Kue

// phone numbers to be blacklisted
const blacklist = [
    '4153518780',
    '4153518781'
]

function sendNotification(phoneNumber, message, job, done) {
    // sendNotification function
    if (blacklist.includes(phoneNumber)) { // if the phone number is in the blacklist
        start_progress = job.progress(0, 100); // track the job progress 0 out of 100
        queue.on('error', function(err) { // on err
            console.log(`Phone number ${phoneNumber} is blacklisted`); // log to the console the phone number
        })
    } else {
        new_progress = job.progress(50, 100); // track the job progress 50 out of 100
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`); // log message to the console
    };
};