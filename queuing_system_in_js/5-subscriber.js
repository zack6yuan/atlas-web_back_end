const redis = require('redis')

try {
    await client.connect()
    console.log("Redis client connected to the server")
} catch (err) {
    (`Redis client not connected to the server: ${err}`)
}

(async () => {
    const client = redis.createClient()
    const subscriber = client.duplicate()
    await subscriber.connect()
    await subscriber.subscribe('holberton school channel', (message) => {
        if message === "KILL_SERVER" {
            subscriber.unsubscribe()
            subscriber.quit()
        } else {
            console.log(message)
        }
    })
})