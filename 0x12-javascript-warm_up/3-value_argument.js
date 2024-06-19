#!/usr/bin/node

// This script prints the first argument passed to it.

const i = 2;
if (process.argv[i]) {
  console.log(process.argv[i]);
} else if (process.argv[i] === undefined) {
  console.log('No argument');
}
