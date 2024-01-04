#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 100-starwars_characters.js <movie-id>');
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

    // Function to fetch character name from URL
    const getCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request(url, { json: true }, (err, res, body) => {
          if (err) {
            reject(err);
          } else if (res.statusCode !== 200) {
            reject(new Error(`Error: ${res.statusCode} - ${body.detail}`));
          } else {
            resolve(body.name);
          }
        });
      });
    };

    // Fetch character names and print them
    Promise.all(charactersUrls.map(url => getCharacterName(url)))
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  }
});
