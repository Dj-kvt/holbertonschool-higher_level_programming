#!/usr/bin/node

// Get the first argument passed to the script and try to convert it to an integer
const x = parseInt(process.argv[2]);

// Check if x is not a number (invalid or missing input)
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Loop x times and print "C is fun" each time
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
