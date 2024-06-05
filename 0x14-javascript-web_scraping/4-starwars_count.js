#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const actorID = 'https://swapi-api.alx-tools.com/api/people/18/';

request(URL, (err, res, body) => {
  let count = 0;
  if (err) throw err;
  const films = JSON.parse(body).results;
  for (const ele of films) {
    if (ele.characters.includes(actorID)) {
      count++;
    }
  }
  console.log(count);
});
