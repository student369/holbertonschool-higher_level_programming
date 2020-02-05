#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject['incr'] = function () {
  let retval = this.value += 1;
  return retval;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
