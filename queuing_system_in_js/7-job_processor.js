const kue = require('kue')
const queue = kue.createQueue()

const blacklist = [
    '4153518780',
    '4153518781'
]

function sendNotification(phoneNumber, message, job, done) {
    // track the progress of the job of 0 out of 100
    if (blacklist.includes(phoneNumber)) {
        queue.on('error', function(err) {
            console.log(`Phone number ${phoneNumber} is blacklisted`)
        })
    } else {
        // Track the progress to 50%
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
    }
}