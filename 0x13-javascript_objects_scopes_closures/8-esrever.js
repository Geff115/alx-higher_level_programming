#!/usr/bin/node

/*
 * This function returns a reversed version of a list.
 * list: The list to reverse.
 */

exports.esrever = function (list) {
  const revElement = [];
  const listLength = list.length;
  for (let i = listLength - 1; i >= 0; i--) {
    revElement.push(list[i]);
  }
  return (revElement);
};
