#!/usr/bin/node

/*
 * This function returns the number of occurences
 * in a list.
 * list: The number of elements to iterate through.
 */

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter = counter + 1;
    }
  }
  return (counter);
};
