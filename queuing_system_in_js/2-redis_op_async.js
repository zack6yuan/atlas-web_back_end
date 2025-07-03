const redis = require('redis') // use the redis module
const client = redis.createClient() // create a redis client
try {
    await client.connect() // try to connect
    console.log("Redis client connected to the server") // log to the console
} catch (err) { // if error
    console.log(`Redis client not connected to the server ${err}`) // log to the console with error message
}

function setNewSchool(schoolName, value) {
    /*
    params -->
    schoolName - name of the school
    value - value of the school

    methods -->
    sets in Redis the value for the key schoolName

    returns -->
    nothing
    */
    redis.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
     /*
    ASYNC FUNCTION

    params -->
    schoolName - name of the school

    methods -->
    get the value of the school name

    returns -->
    logs to the console the value
    */
    value = await redis.get(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton'); // call displaySchoolValue with arg
setNewSchool('HolbertonSanFrancisco', '100'); // call setNewSchool with arg
displaySchoolValue('HolbertonSanFrancisco'); // call displaySchoolValue with arg