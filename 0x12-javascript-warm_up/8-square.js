#!/usr/bin/node

// This script prints a square with
// the given size in the command line.

const sizeOfSquare = process.argv[2];
const convertSize = Math.floor(Number(sizeOfSquare));
let rowString;

if (isNaN(convertSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convertSize; i++) {
    rowString = '';
    for (let j = 0; j < convertSize; j++) {
      rowString += 'X';
    }
    console.log(rowString);
  }
}
