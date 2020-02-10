#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w > 0 && w !== undefined) && (h > 0 && h !== undefined)) {
    this.width = w;
    this.height = h;
  }
  this.print = function (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  };
};
