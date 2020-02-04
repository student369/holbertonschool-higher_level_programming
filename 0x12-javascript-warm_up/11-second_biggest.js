#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  let largest = process.argv[2];
  let secondLargest = process.argv[3];
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > largest) {
      secondLargest = largest;
      largest = parseInt(process.argv[i]);
    }
    if (parseInt(process.argv[i]) > secondLargest && parseInt(process.argv[i]) < largest) {
      secondLargest = parseInt(process.argv[i]);
    }
  }
  console.log(secondLargest);
}
