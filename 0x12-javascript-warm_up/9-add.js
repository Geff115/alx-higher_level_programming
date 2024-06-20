#!/usr/bin/node

/*
 * add - This function adds two integers.
 * a: The first integer.
 * b: The second integer.
 * return: The addition of a and b.
 */
const a = Math.floor(Number(process.argv[2]));
const b = Math.floor(Number(process.argv[3]));

function add (a, b) {
  if (a === undefined && b === undefined) {
    console.log('NaN');
  } else if (isNaN(a) && isNaN(b)) {
    console.log('NaN');
  } else if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else if (a !== undefined && b !== undefined) {
    console.log(a + b);
  }
}
add(a, b);
