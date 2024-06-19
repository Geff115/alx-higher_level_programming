#!/usr/bin/node

// This scrpt prints two arguments passed to it.

const i = 2;
const j = 3;
if (process.argv[i] && process.argv[j]) {
  console.log(process.argv[i] + ' is ' + process.argv[j]);
} else if (process.argv[i] && process.argv[j] === undefined) {
  console.log(process.argv[i] + ' is ' + process.argv[j]);
} else if (process.argv.length <= 2) {
  console.log(process.argv[i] + ' is ' + process.argv[j]);
}
