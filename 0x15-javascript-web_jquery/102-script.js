$(function () {
  $('input#btn_translate').on('click', () => {
    if ($('input#language_code').val()) {
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('input#language_code').val()}`, (data) => {
        $('div#hello').text(data.hello);
      });
    }
  });
});
