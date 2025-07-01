const redis = require('redis')
const client = redis.createClient()

try {
    await client.connect()
    console.log("Redis client connected to the server")
} catch (err) {
    (`Redis client not connected to the server: ${err}`)
}