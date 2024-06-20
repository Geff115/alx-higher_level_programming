#!/usr/bin/node

// This script computes and prints a factorial

const arg = Math.floor(Number(process.argv[2]));

function factorial (arg) {
  if (arg === undefined) {
    return (1);
  } else if (isNaN(arg)) {
    return (1);
  } else if (arg <= 1) {
    return (1);
  } else if (arg > 1) {
    return (arg * factorial(arg - 1));
  }
}
console.log(factorial(arg));
