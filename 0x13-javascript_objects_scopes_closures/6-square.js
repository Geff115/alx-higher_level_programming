#!/usr/bin/node

// This is a Square inherits from a Sqyare class
// in a file 5-square.js.

const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.export = Square;
