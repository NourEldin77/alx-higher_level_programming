#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(URL, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
