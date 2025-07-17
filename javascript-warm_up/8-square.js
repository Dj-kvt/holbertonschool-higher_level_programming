#!/usr/bin/node

// Parse the first argument as an integer
const size = parseInt(process.argv[2]);

// Check if the size is a valid number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Print a square of size x size using 'X'
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
