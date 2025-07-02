const express = require('express')
const app = express()
port = 7865

app.get('/', (req, res) => {
    res.send('Welcome to the payment system')
})

app.get('/cart/:id', (req, res) => {
    res.send(`Payment methods for cart: ${id}`)
})

app.get('/available_paymets', (req, res) => {
    data = {
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    }
    res.send(data)
})

app.post('/login', (req, res) => {
    res.send(`Welcome: userName`)
})

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`)
})