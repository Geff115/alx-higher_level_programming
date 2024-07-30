#!/usr/bin/node
/**
 * Using the fs module in Node.js for file system functionalities.
 * Using readFile function from the fs module to read a file.
 */
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  console.log(data);
});
