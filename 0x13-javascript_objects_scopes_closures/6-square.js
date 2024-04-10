#!/usr/bin/node
const Squaree = require('./5-square');

class Square extends Squaree {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      super.printSymbol = c;
    }
    super.print();
  }
}
module.exports = Square;
