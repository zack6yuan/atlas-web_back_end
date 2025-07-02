// This is the module for task 16, In stock?
const express = require('express')
const app = express()

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
    for (item of listProducts) {
        if (item.id === id) {
            return item
        }
    }
}

app.get('/list_products', (req, res) => {
    res.send(listProducts)
})

const redis = require('redis')
const client = redis.createClient()

try {
    await client.connect()
    console.log("Redis client connected to the server")
} catch (err) {
    console.log(`Redis client not connected to the server ${err}`)
}

function reserveStockById(itemId, stock) {
    // Set in Redis the stock for the key item.Item_ID
}

async function getCurrentReservedStockById(itemID) {
    // Return the reserved stock for a specific item
}

app.get('/list_products/:itemId', (req, res) => {
    getCurrentReservedStockById()
})

app.get('/reserve_product/:itemId', (req, res) => {
    
})