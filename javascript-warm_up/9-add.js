#!/usr/bin/node

// Define the add function as required
function add(a, b) {
  return a + b;
}

// Parse both arguments
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// Print the result of the addition (NaN if any argument is invalid)
console.log(add(a, b));
