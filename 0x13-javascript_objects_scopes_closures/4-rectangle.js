#!/usr/bin/node

/*
 * This is a Rectangle class.
 * The constructor takes two arguments, w and h.
 * If w or h is equal to 0 or not a positive integer,
 * create an empty object.
 * Create an instance method called print() that prints
 * the rectangle using the character X.
 * Create an instance method called rotate() that exchanges
 * the width and the height of the rectangle.
 * Create an instance method called double() that multiples
 * the width and the height of the rectangle by 2.
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === undefined && this.height === undefined) {
      return;
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
