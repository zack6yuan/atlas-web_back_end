const redis = require('redis') // use the redis module

try {
    await client.connect() // try to connect
    console.log("Redis client connected to the server") // log success messsage to the console
} catch (err) { // if error
    (`Redis client not connected to the server: ${err}`) // log error message to the console
}

(async () => {
    /*
    ASYNC FUNCTION
    */
    const client = redis.createClient() // crete a Redis client
    const subscriber = client.duplicate() // create a separate connection
    await subscriber.connect() // try to connect
    await subscriber.subscribe('holberton school channel', (message) => {
        if (message === "KILL_SERVER") { // if the message is "KILL SERVER"
            subscriber.unsubscribe() // unsubscribe
            subscriber.quit() // quit
        } else {
            console.log(message) // log messag to the console
        }
    })
})