#!/usr/bin/node

// This script searches the second biggest integer
// in the list of elements.

const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  for (let i = 0; i < sortedArgs.length; i++) {
    if (sortedArgs[i] !== sortedArgs[0]) {
      console.log(sortedArgs[i]);
      break;
    }
  }
}
