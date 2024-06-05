#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const textToWrite = process.argv[3];

function readfile (filename, txt) {
  fs.writeFile(filename, txt, 'utf8', (err) => { if (err) throw err; });
}

readfile(filename, textToWrite);
