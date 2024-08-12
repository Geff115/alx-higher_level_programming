/**
 * This script uses jQuery to update the text of the <header> element to
 * New Header!!! when the user clicks on DIV#update_header.
 */

/* global $ */

$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
