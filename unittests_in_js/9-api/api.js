const express = require('express')
const app = express()
port = 7865

app.get('/', (req, res) => {
    res.send('Welcome to the payment system')
})

app.get('/cart/:id', (req, res) => {
    res.send(`Payment methods for cart: ${id}`)
})

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`)
})