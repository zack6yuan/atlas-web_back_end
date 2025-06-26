#!/usr/bin/env node
// program 1-stdin.js that is executed through the command line
const readline = require("readline")

const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

input.question(`Welcome to Holberton School, what is your name? \n`, name => {
    console.log(`Your name is: ${name}`);
    console.log("This important software is now closing \n");
    input.close()
})