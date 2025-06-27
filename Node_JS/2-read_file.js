#!/usr/bin/env node
// function countStudents using database.csv
function countStudents() {
    const fs = require('fs');
    const data = fs.readFileSync('./database.csv')
    if (!(data)) {
        console.log("Cannot load the database")
    }
}


module.exports = countStudents()