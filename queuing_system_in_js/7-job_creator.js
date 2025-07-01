const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const kue = require('kue')
const queue = kue.createQueue()

for (x = 0; x < jobs.length; x++) {
    queue.create('push_notification_code_2', {
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