const { createPushNotificationsJobs } = require('./8-job');
const kue = require('kue');
const queue = kue.createQueue();

before(function() {
    queue.testMode.enter();
});

afterEach(function() {
    queue.testMode.clear();
});

after(function() {
    queue.testMode.exit();
});

// Test that the one job from 8-job.js is inside the queue
it('validates which jobs are inside the queue', function() {
    expect(queue.testMode.jobs.length).to.equal(1);
});