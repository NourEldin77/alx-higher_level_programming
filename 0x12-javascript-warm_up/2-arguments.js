#!/usr/bin/node

const { argv } = require('node:process');

argv[2] !== undefined ? console.log('Argument found') : console.log('No argument');
