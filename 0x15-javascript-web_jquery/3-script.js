/**
 * This script adds the class red to the <header> element when
 * the user clicks on the tag DIV#red_header
 * using the jQuery api: https://code.jquery.com/jquery-3.2.1.min.js
 */

/* global $ */

$('#red_header').click(function () {
  $('header').addClass('red');
});
