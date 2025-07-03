// This is the module for task 16, In stock?
const express = require('express') // require the express module
const app = express() // assign to the variable "app"

const listProducts = [
    {
        id: 1,
        name: "Suitcase 250",
        price: 50,
        stock: 4
    },
    {
        id: 2,
        name: "Suitcase 450",
        price: 100,
        stock: 10
    },
    {
        id: 3,
        name: "Suitcase 650",
        price: 350,
        stock: 2
    },
    {
        id: 4,
        name: "Suitcase 1050",
        price: 500,
        stock: 5
    }
]

function getItemById(id) {
    for (item of listProducts) { // get the item in array listProducts
        if (item.id === id) { // if the id matches
            return item // reutrn the item
        }
    }
}

app.get('/list_products', (req, res) => {
    res.send(listProducts)
})

const redis = require('redis') // require the redis module
const client = redis.createClient() // create a redis client

try {
    await client.connect() // try to connect
    console.log("Redis client connected to the server") // log success message to the console
} catch (err) { // if error
    console.log(`Redis client not connected to the server ${err}`) // log the error message to the console
}

function reserveStockById(itemId, stock) {
    // Set in Redis the stock for the key item.Item_ID
    client.set(itemId, stock)
}

async function getCurrentReservedStockById(itemID) {
    // Return the reserved stock for a specific item
    console.log(itemID)
}

app.get('/list_products/:itemId', (req, res) => {
    getCurrentReservedStockById()
})

app.get('/reserve_product/:itemId', (req, res) => {
    if (listProducts.includes(item)) {
        if (stock > 1) {
            console.log({"status":"Reservation confirmed","itemId":1})
        } else if (stock < 1) {
            console.log({"status":"Not enough stock available","itemId":1})
        } else {
            console.log({"status":"Product not found"})
        }
    }
})