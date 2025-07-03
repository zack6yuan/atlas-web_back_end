#!/usr/bin/env node
// function countStudents using database.csv
function countStudents() {
    // require fs (file system) module
    const fs = require('fs');
    // reads data from the csv file
    const data = fs.readFileSync('./database.csv')
    // if there is no data
    if (!(data)) {
        // log to the console
        console.log("Cannot load the database")
    }
}

// export the module
module.exports = countStudents;