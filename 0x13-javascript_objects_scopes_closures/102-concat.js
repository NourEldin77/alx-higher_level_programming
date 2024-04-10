#!/usr/bin/node

const fs = require('fs');

function oneFile (a, b, c) {
  fs.readFile(a, 'utf8', (e, d) => {
    if (e) {
      console.error(`Error reading ${a}: ${e}`);
      return;
    }
    fs.readFile(b, 'utf8', (e, d2) => {
      if (e) {
        console.error(`Error reading ${b}: ${e}`);
        return;
      }
      const cc = d + d2;
      fs.writeFile(c, cc, 'utf8', (e) => {
        if (e) {
          console.error(`Error writing to ${c}: ${e}`);
        }
      });
    });
  });
}

if (process.argv.length === 5) {
  const a = process.argv[2];
  const b = process.argv[3];
  const c = process.argv[4];
  oneFile(a, b, c);
} else {
  console.error('Usage: ./102-concat.js fileA fileB fileC ');
}
