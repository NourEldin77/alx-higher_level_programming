#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
function readfile (filename) {
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      throw err;
    } else {
      console.log(data);
    }
  });
}

readfile(filename);
