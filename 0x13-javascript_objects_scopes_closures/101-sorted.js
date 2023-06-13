#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

for (const user in dict) {
  const count = dict[user];

  if (!newDict[count]) {
    newDict[count] = [];
  }

  newDict[count].push(user);
}

console.log(newDict);
