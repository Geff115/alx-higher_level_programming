#!/usr/bin/node

/*
 * This class Rectangle uses a constructor with two arguments.
 * w and h are the arguments.
 * if w or h is equal to 0 or not a positive integer,
 * create an empty object.
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return ({});
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
