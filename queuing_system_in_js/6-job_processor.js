const kue = require('kue')
const queue = kue.createQueue()

queue.create('push_notification_code', {
    phoneNumber: String,
    message: String
}).save()

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message ${message}`)
}

queue.create('push_notification_code', {
    phoneNumber: String,
    message: String
}).save()

queue.on('job enqueue', function(phoneNumber, message) {
    sendNotification(phoneNumber, message)
})