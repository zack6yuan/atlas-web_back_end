const redis = require('redis')
const client = redis.createClient()

try {
    await client.connect()
    console.log("Redis client connected to the server")
} catch (err) {
    console.log(`Redis client not connected to the server ${err}`)
}

function setNewSchool(schoolName, value) {
    redis.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    value = redis.get(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');