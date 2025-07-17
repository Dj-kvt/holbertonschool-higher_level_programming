#!/usr/bin/node

// Get the first argument passed to the script (ignoring the first 2 elements)
const arg = process.argv[2];

// If no argument is passed, print "No argument"
if (arg === undefined) {
  console.log('No argument');
} else {
  // Otherwise, print the argument
  console.log(arg);
}
