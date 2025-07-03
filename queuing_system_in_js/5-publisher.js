const redis = require('redis') // use the redis module
const client = redis.createClient() // create a redis client

try {
    await client.connect() // try to connect
    console.log('Redis client connected to the server') // log success message to the console
} catch (err) { // if error
    console.log(`Redis client not connected to the server: ${err}`) // log error message to the console
}

function publishMessage(message, time) {
    /*
    params:
    message --> string
    time --> integer - in ms

    methods:
    publishes to the channel "holberton school"
    */
    const publisher = redis.createClient()
    console.log(`About to send ${message}`)
    publisher.publish('holberton school channel', JSON.stringify(message), time)
}

publishMessage("Holberton Student #1 starts course", 100); // publish after 100ms
publishMessage("Holberton Student #2 starts course", 200); // publish after 200ms
publishMessage("KILL_SERVER", 300); // publish after 300ms
publishMessage("Holberton Student #3 starts course", 400); // publish after 400ms