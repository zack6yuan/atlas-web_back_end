const kue = require('kue')
const queue = require('queue')

queue.create('push_notification_code', {
    phoneNumber: String,
    message: String
}).save()

queue