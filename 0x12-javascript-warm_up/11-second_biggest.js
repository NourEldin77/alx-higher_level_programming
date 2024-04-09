#!/usr/bin/node

const arrVec = process.argv.slice(2);

if (arrVec.length === 0 || arrVec.length === 1) {
  console.log(0);
} else {
  arrVec.splice(arrVec.indexOf(String(Math.max(...arrVec))), 1);
  console.log(Math.max(...arrVec));
}
