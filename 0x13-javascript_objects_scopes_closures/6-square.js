#!/usr/bin/node

const Sqr = require('./5-square').Square;

function Square (size) {
  Sqr.call(this, size);
}

Square.prototype = Object.create(Square.prototype);
Square.constructor = Square;

Square.prototype.charPrint = function (c = 'X') {
  this.print(c);
};

exports.Square = Square;
