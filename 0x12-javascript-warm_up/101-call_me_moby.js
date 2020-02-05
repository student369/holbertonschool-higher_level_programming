#!/usr/bin/node
exports.callMeMoby = function (n, func) {
  for (let i = 0; i < n; i++) {
    func();
  }
};
