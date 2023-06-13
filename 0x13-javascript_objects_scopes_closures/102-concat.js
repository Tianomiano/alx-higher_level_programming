#!/usr/bin/node
const fs = require('fs');
const fileA =require('./fileA')
const fileB =require('./fileB')

const fileApath = process.argv[fileA];
const fileBpath = process.argv[fileB];
const dest = process.argv[fileC];

const fileAdata = fs.readFileSync(fileA, 'utf8');
const fileBdata = fs.readFileSync(fileB, 'utf8');
const concatData = fileAdata + fileBdata;

fs.writeFileSync(dest, concatData, 'utf8');
