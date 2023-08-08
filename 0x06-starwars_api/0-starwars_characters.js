#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, response, body) {
    if (err) throw err;
    // console.log(JSON.parse(body).title);
    for (const i in JSON.parse(body).characters) {
        request(JSON.parse(body).characters[i], function (err, response, body) {
            if (err) throw err;
            console.log(JSON.parse(body).name);
        });
    }
    }
);
