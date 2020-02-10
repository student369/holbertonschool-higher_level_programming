#!/usr/bin/node

const fs = require('fs');
for (let i = 2; i < 4; i++) {
  fs.readFile(process.argv[i], function read (err, data) {
    if (err) {
      console.log(err);
    }
    const content = data;
    fs.appendFileSync('fileC', content);
  });
}
