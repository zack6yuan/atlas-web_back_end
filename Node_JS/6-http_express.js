#!/usr/bin/env node
// Small HTTP server using the Express module
const express = require('express')
const app = express()
const port = 1245

app.get('/', (req, res) => {
    res.send('Hello World!')
})