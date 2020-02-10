#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w > 0 && w !== undefined) && (h > 0 && h !== undefined)) {
    this.width = w;
    this.height = h;
  }
};
