#!/usr/bin/node
/**
 * Using the request module's get method to make a GET request to
 * the Star Wars API.
 */
const request = require('request');
let bodyResponse;
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  bodyResponse = JSON.parse(body);
  console.log(bodyResponse.title);
});
