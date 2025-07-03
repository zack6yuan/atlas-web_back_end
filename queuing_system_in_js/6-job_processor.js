const kue = require('kue') // require the Kue module
const queue = kue.createQueue() // create a queue with Kue

queue.create('push_notification_code', { // create a queue named "push_notificaton_code"
    // Job data
    phoneNumber: String,
    message: String
}).save()

function sendNotification(phoneNumber, message) {
    /*
    params:
    phoneNumber --> user's phoneNumber
    message --> message to be sent
    */
   // Send message to phone number according to format
    console.log(`Sending notification to ${phoneNumber}, with message ${message}`)
}

queue.create('push_notification_code', { // create a queue named 
    phoneNumber: String,
    message: String
}).save()

queue.on('job enqueue', function(phoneNumber, message) {
    sendNotification(phoneNumber, message)
})