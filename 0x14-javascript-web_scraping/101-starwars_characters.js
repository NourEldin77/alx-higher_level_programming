#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(URL, (err, res, body) => {
  if (err) throw err;
  const actors = JSON.parse(body).characters;

  const reqAndPrint = async () => {
    for (const actor of actors) {
      await new Promise((resolve, reject) => {
        request(actor, (err, res, body) => {
          if (err) reject(err);
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  };

  reqAndPrint().catch(console.error);
});
