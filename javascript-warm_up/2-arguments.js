#!/usr/bin/node

// Get all command-line arguments passed to the script, excluding the first two (node and script path)
const args = process.argv.slice(2);

// Check how many arguments were provided
if (args.length === 0) {
  // No arguments passed
  console.log('No argument');
} else if (args.length === 1) {
  // Exactly one argument passed
  console.log('Argument found');
} else {
  // More than one argument passed
  console.log('Arguments found');
}
