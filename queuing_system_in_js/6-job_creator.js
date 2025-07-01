const kue = require('kue')
const queue = kue.createQueue()

queue.create('push_notification_code', {
    phoneNumber: String,
    message: String
}).save()

queue.on('error', function() {
    console.log('Notification job failed')
})

queue.on('job complete', function() {
    console.log('Notification job completed')
})

queue.on('job complete', function(id) {
    console.log(`Notification job created: ${id}`)
})