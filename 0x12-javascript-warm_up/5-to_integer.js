#!/usr/bin/node

// This script prints My number: <The number>. If the number can
// be converted to an integer.

const arg = process.argv[2];
const num = Math.floor(Number(arg));

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
