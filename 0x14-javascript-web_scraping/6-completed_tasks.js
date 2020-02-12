#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const completetasks = {};
    const todos = JSON.parse(body);
    for (const task in todos) {
      if (todos[task].completed === true) {
        if (completetasks[todos[task].userId]) completetasks[todos[task].userId]++;
        else completetasks[todos[task].userId] = 1;
      }
    }
    console.log(completetasks);
  }
});
