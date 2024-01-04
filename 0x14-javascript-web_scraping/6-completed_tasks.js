#!/usr/bin/node
// Computes the num of tasks completed by user-id
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 6-completed_tasks.js <api-url>');
  process.exit(1);
}

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${body}`);
  } else {
    const completedTasksByUser = {};

    body.forEach((task) => {
      if (task.completed) {
        const userId = task.userId.toString();

        if (completedTasksByUser[userId]) {
          completedTasksByUser[userId]++;
        } else {
          completedTasksByUser[userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});

