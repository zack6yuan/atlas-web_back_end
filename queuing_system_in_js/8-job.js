const kue = require('kue') // require the Kue module
const queue = kue.createQueue() // create a queue with Kue

function createPushNotificationsJobs(jobs, queue) {
    if (typeof jobs !== 'array') { // if jobs is not an array
        throw new Error('Jobs is not an array') // throw an error with message
    }
    for (let x = 0; x < jobs.length; x++) { // loop through jobs array
        queue.create('push_notification_code_3', {
            jobs
        }).save()
        // Job created with no error
        queue.on('job enqueue', function(id) {
            console.log(`Notification job created: ${id}`)
        })
        // Job is completed
        queue.on('job complete', function(id) {
            console.log(`Notification job ${id} completed`)
        })
        // Job created experiences error
        queue.on('error', function(err, id) {
            console.log(`Notification job ${id} failed: ${err}`)
        })
        // Log job progress to the console
        queue.on('progress', function(progress, id) {
            console.log(`Notification job  ${id} ${progress} complete`)
        })
    }
}