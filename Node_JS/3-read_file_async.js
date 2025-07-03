// function countStudents using database.csv
function countStudents(path) {
    return new Promise((resolve, reject) => {
        const fs = require('fs')
        try {
            data = fs.readFileSync('./database.csv')
        } catch (err) {
            console.log(`Canot load the database: ${err}`)
        }
        group_size = (data[0], data[-1]).length
    })





    /* 
    return Promise.resolve) => {
        const fs = require('fs')
        data == fs.readFileSync('./database.csv')
        if (!(data)) {
            console.log('Cannot load the database')
        }
    })

        const fs = require('fs');
        data == fs.readFileSync('./database.csv');
        if (!(data)) {
            console.log('Cannot load the database')
        }
        return Promise.resolve({
            console.log("What is your name?")
        })
            */

        
}

// export the module
module.exports = countStudents;