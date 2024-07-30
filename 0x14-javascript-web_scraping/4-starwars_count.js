#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const actorID = 'https://swapi-api.alx-tools.com/api/people/18/';

request(URL, (err, res, body) => {
  if (err) throw err;
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    if (film.characters.includes(actorID)) {
      count++;
    }
  }
  console.log(count);
});
