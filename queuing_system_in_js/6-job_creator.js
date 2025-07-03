const kue = require('kue') // require the Kue module
const queue = kue.createQueue() // create a queue with Kue

queue.create('push_notification_code', { // create a queue named "push_notification_code"
    // Job data
    phoneNumber: String,
    message: String
}).save()

// Job created experiences error
queue.on('error', function() {
    console.log('Notification job failed')
})

// Job is successfully creted (log with id)
queue.on('job enqueue', function(id) {
    console.log(`Notification job created: ${id}`)
})

// Job is completed
queue.on('job complete', function() {
    console.log('Notification job completed')
})