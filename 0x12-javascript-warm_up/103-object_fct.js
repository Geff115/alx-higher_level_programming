#!/usr/bin/node

// This incr increments the integer value.

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
