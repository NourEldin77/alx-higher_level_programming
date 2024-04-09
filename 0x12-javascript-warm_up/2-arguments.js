#!/usr/bin/node

const { argv } = require('node:process');

const arrvec = argv.length;
arrvec === 3 ? console.log('Argument found') : arrvec > 2 ? console.log('Arguments found') : console.log('No argument');
