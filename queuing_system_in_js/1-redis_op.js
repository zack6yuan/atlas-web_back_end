import { createClient } from 'redis';
const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
await client.connect();
console.log("Redis client connected to the server");

function setNewSchool(schoolName, value) {
    redis.set(schoolName, value);
    redis.print("Values set!");
}

function displaySchoolValue(schoolName) {
    value = redis.get(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');