#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  if (n > 0) {
    for (let i = 0; i < n; i++) {
      let newLine = '';
      for (let j = 0; j < n; j++) {
        newLine += 'X';
      }
      console.log(newLine);
    }
  }
}
