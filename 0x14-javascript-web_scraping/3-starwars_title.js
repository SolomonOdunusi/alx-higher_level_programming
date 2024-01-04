#!/usr/bin/node
// prints the title of a Star Wars movie 
// has a given int
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 3-starwars_title.js <movie-id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${body.detail}`);
  } else {
    console.log(body.title);
  }
});
