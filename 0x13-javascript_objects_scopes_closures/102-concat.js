#!/usr/bin/node

// This script concatenates 2 files

const fs = require('fs');

const fA = fs.readFileSync(process.argv[2], 'utf8');
const fB = fs.readFileSync(process.argv[3], 'utf8');
const answer = fA + fB;
fs.writeFile(process.argv[4], answer, function (err) { if (err) throw err; });
