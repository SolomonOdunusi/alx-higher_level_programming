#!/usr/bin/node
// Prints the number of movies
// that has “Wedge Antilles”
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <api-url>');
  process.exit(1);
}

const characterId = 18;

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${body.detail}`);
  } else {
    const films = body.results;
    const count = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  }
});
