#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 101-starwars_characters.js <movie-id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${body.detail}`);
  } else {
    const charactersUrls = body.characters;

    // Fetch and print character names in the same order
    charactersUrls.forEach(url => {
      request(url, { json: true }, (err, res, character) => {
        if (err) {
          console.error(err);
        } else if (res.statusCode !== 200) {
          console.error(`Error: ${res.statusCode} - ${character.detail}`);
        } else {
          console.log(character.name);
        }
      });
    });
  }
});
