#!/usr/bin/env node
// Small HTTP server using the http module
const app = require('http')

app.createServer((request, response) => {
    response.write("Hello Holberton School!");
    response.end()
}).listen(1245);

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    res.send(`This is the list of our students`)
})