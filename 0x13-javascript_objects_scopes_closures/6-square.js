#!/usr/bin/node

/*
 * This is a Square class.
 * This class inherits from a Rectangle class.
 * Created a method called charprint(c) that prints the rectangle using
 * the character c.
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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

class NewSquare extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

exports.Rectangle = Rectangle;
exports.Square = Square;
exports.NewSquare = NewSquare;
