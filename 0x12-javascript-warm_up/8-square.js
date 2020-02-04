#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let s = '';
    for (let j = 0; j < process.argv[2]; j++) {
      s += 'X' + '';
    }
    console.log(s);
  }
}
