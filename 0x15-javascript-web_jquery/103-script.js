/**
 * This script uses jQuery:
 * fetches and prints how to say “Hello” depending on the language
 * using this API service: https://www.fourtonfish.com/hellosalut/hello/
 * The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
 * The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
 * The translation of “Hello” must be displayed in the HTML tag DIV#hello
 */

/* global $ */

$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: langCode },
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
