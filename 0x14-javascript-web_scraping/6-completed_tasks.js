#!/usr/bin/node
/**
 * Using the request module's get method to send a GET request to
 * a provided API URL and then process the response to count the
 * number of completed tasks for each user.
 */
const request = require('request');
let bodyResponse;
request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  bodyResponse = JSON.parse(body);
  const emptyObject = {};
  for (let i = 0; i < bodyResponse.length; i++) {
    if (bodyResponse[i].completed === true) {
      if (emptyObject[bodyResponse[i].userId]) {
        emptyObject[bodyResponse[i].userId] += 1;
      } else {
        emptyObject[bodyResponse[i].userId] = 1;
      }
    }
  }
  console.log(emptyObject);
});
