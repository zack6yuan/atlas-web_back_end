const kue = require('kue')
const queue = kue.createQueue()

queue.create('push_notification_code', {
    phoneNumber: String,
    message: String
}).save()

// Job created experiences error
queue.on('error', function() {
    console.log('Notification job failed')
})

// Job is successfully creted
queue.on('job enqueue', function(id) {
    console.log(`Notification job created: ${id}`)
})

// Job is completed
queue.on('job complete', function() {
    console.log('Notification job completed')
})