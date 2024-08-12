/**
 * This script uses jQuery to fetch and list the title for all movies
 * by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
 * All movie titles must be list in the HTML tag UL#list_movies
 */

/* global $ */

$.ajax('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then(function (data) {
    data.results.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
