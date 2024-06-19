#!/usr/bin/node

// This script prints x times "C is fun"

const x = process.argv[2];
const num = Math.floor(Number(x));

if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
