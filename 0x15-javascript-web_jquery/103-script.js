$(function () {
  function callback () {
    if ($('input#language_code').val()) {
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('input#language_code').val()}`, (data) => {
        $('div#hello').text(data.hello);
      });
    }
  }
  $('input#btn_translate').on('click', callback);
  $('input#btn_translate').on('keypress', (e) => {
    if (e.key == 'Enter') {
      callback();
    }
  });
});
