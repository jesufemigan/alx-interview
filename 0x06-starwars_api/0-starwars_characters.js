#!/usr/bin/node

const request = require("request");
const movie_id = process.argv[2];

request(
  "https://swapi-api.alx-tools.com/api/films/" + movie_id,
  (err, res, body) => {
    if (err) throw err;
    const actors = JSON.parse(body).characters;
    getActors(actors, 0);
  }
);

const getActors = (actors, n) => {
  if (x == actors.length) return;
  request(actors[n], (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    getActors(actors, n + 1);
  });
};
