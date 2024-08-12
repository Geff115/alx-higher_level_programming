/**
 * This script uses jQuery and it fetches the character name from
 * this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
 * The name must be displayed in the HTML tag DIV#character
 */

/* global $ */

$.ajax('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then(function (data) {
    $('#character').text(data.name);
  });
