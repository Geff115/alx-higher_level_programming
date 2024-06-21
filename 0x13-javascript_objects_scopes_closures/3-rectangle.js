#!/usr/bin/node

/*
 * This is a Rectangle class.
 * The constructor takes two arguments w and h.
 * if w or h is equal to 0 or not a positive integer, it creates
 * an empty object.
 * Creates an instance method called print, to print the rectangle
 * using the character X.
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
}

module.exports = Rectangle;
