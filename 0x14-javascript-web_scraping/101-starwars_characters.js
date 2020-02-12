#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    const promiselist = [];
    for (const character in characters) {
      const namepromise = new Promise(resolve => {
        request(characters[character], function (err, res, body) {
          if (err) console.log(err);
          else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      promiselist.push(namepromise);
    }
    Promise.all(promiselist).then(function (namelist) {
      for (const name in namelist) {
        console.log(namelist[name]);
      }
    });
  }
});
