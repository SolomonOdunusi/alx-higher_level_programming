#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  process.exit(1);
}
const [, , f1, f2, f3] = process.argv;

fs.readFile(f1, 'utf8', (error1, data1) => {
  if (error1) {
    process.exit(1);
  }

  fs.readFile(f2, 'utf8', (error2, data2) => {
    if (error2) {
      process.exit(1);
    }

    const concatenatedContent = `${data1}${data2}`;
    fs.writeFile(f3, concatenatedContent, 'utf8', (error3) => {
      if (error3) {
        process.exit(1);
      }
    });
  });
});
