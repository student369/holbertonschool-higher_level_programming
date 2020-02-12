#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    let wedgefilms = 0;
    const films = JSON.parse(body).results;
    for (const film in films) {
      const characters = films[film].characters;
      for (const character in characters) {
        if (characters[character].search(/18\/$/) > -1) wedgefilms++;
      }
    }
    console.log(wedgefilms);
  }
});
