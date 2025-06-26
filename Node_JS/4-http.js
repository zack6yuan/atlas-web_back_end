#!/usr/bin/env node
// Small HTTP server using the http module
const http = require('http')

http.createServer((request, response) => {
    response.write("Hello Holberton School!");
    response.end()
}).listen(1245);