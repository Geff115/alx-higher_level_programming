/**
 * This script uses jQuery to toggles the class of the <header> element
 * when the user clicks on the tag DIV#toggle_header.
 * The <header> element must always have one class: red or green,
 * never both classes at the same time and never empty.
 * If the current class is red, when the user click on DIV#toggle_header,
 * the class must be updated to green ; and the reverse.
 */

/* global $ */

$('#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
