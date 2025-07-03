const redis = require('redis') // use the redis module
const client = redis.createClient() // create a redis client

try {
    await client.connect() // wait for the connection
    console.log("Redis client connected to the server") // connection message
} catch (err) { // if error
    console.log(`Redis client not connected to the server ${err}`) // log to console with error mesage
}