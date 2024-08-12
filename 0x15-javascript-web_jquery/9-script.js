/**
 * This script uses jQuery to fetch from from https://hellosalut.stefanbohacek.dev/?lang=fr
 * and displays the value of hello from that fetch in the HTML tag DIV#hello.
 * The translation of “hello” must be displayed in the HTML tag DIV#hello.
 */

/* global $ */

$(document).ready(function () {
  $.ajax('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(function (data) {
      $('#hello').text(data.hello);
    });
});
