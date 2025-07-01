const redis = require('redis')
const client = redis.createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
await client.connect();
console.log("Redis client connected to the server");

function setNewSchool(schoolName, value) {
    redis.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    value = await redis.get(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');