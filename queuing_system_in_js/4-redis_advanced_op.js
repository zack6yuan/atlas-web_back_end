const redis = require('redis') // use the redis module
const client = redis.createClient() // create a redis client

try {
    await client.connect() // try to connect
    console.log("Redis client connected to the server") // log success message to the console
} catch (err) { // if error
    console.log(`Redis client not connected to the server ${err}`) // log error messsage to the console
}

// create a hash and use h.set
const cityHash = await client.hSet(
    // key of the hash (HolbertonSchools)
    'HolbertonSchools',
    {
        // set values
        'Portland': "50",
        'Seattle': '80',
        'New York': '20',
        'Bogota': '20',
        'Cali': '40',
        'Paris': '2'
    }
)

const result = await client.hGetAll('HolbertonSchools') // display the object stores in Redis
console.log(result) // log the result to the console