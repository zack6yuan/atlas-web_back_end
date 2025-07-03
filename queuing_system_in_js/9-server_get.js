const express = require('express') // require the express module
const app = express() // assign to the variable "app"

// array "listProducts"
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
    for (item of listProducts) { // item in listProducts array
        if (item.id === id) { // if the id matches
            return item // reuturn the item
        }
    }
}

app.get('/list_products', (req, res) => {
    res.send(listProducts)
})