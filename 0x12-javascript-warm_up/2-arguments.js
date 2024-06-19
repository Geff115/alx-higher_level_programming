#!/usr/bin/node

/* This script checks for command line arguments.
 * if no arguments are passed to the script, it prints no arguments.
 * if only one argument is passed to the script, it prints argument found.
 * otherwise, prints arguments found.
 */
if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length <= 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
