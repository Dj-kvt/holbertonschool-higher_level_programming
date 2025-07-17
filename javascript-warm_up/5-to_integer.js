#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert to integer using Number()
const num = Number(arg);

// Check if it's a valid number using isNaN()
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(num)}`);
}