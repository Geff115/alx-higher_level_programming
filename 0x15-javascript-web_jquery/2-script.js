/**
 * This script updates the text color of the <header> element to red (#FF0000)
 * when the user clicks on the tag DIV#red_header
 * using jQuery api: https://code.jquery.com/jquery-3.2.1.min.js
 */

/* global $ */

$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
