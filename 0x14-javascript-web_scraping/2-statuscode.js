#!/usr/bin/node
/**
 * Using the request module.
 * Using the request module's get method, which makes a GET request to a
 * specified URL.
 */
let statusC;
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  statusC = response.statusCode;
  console.log('code: ', statusC);
});
