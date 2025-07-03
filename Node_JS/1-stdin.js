#!/usr/bin/env node
// program 1-stdin.js that is executed through the command line
const readline = require("readline") // readline to read the data

// sets up the command line prompt
const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// Asks the question to the console
input.question(`Welcome to Holberton School, what is your name? \n`, name => {
    console.log(`Your name is: ${name}`);
    console.log("This important software is now closing \n");
    // Close the software and the end of the program
    input.close()
})