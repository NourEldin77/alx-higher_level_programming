#!/usr/bin/node

const n = process.argv[2] !== undefined ? parseInt(process.argv[2]) : console.log('Missing number of occurrences');
if (n > 0 && typeof (n) === 'number') {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
