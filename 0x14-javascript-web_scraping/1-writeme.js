#!/usr/bin/node
/**
 * Using the fs module for file system io
 * Using the writeFile function from the fs module to
 * write a string to a file.
 */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.error('Error: ', err);
  }
});
