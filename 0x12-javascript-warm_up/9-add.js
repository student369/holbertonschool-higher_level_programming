#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[2] === 1 && process.argv[3] === undefined)) {
  console.log(NaN);
} else if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(NaN);
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
