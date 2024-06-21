#!/usr/bin/node

// This script prints the number of arguments already printed
// and the new argument value.

let counter = 0;
exports.logMe = function (item) {
  if (item === undefined) {
    return;
  }
  console.log(`${counter}: ${item}`);
  counter += 1;
};
