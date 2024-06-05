#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (err, res, body) => {
  if (err) throw err;
  const result = {};
  const todosObj = JSON.parse(body);
  for (let i = 0; i < todosObj.length; i++) {
    const todo = todosObj[i];
    if (todo.completed && result[todo.userId] === undefined) {
      result[todo.userId] = 1;
    } else if (todo.completed) {
      result[todo.userId]++;
    }
  }
  console.log(result);
});
