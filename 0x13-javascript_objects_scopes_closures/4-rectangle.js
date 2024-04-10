#!/usr/bin/node
class Rectangle {
  static printSymbol = '';
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  printSymbol (c) {
    Rectangle.printSymbol = c;
    return (c);
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      if (Rectangle.printSymbol) {
        console.log(Rectangle.printSymbol.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
