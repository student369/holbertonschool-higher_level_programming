#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (const character in characters) {
      request(characters[character], function (err, res, body) {
        if (err) console.log(err);
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
