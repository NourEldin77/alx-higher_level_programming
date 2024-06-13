$(function () {
  const list = $('ul.my_list');
  $('div#add_item').on('click', () => {
    list.append('<li>Item</li>');
  });
  $('div#remove_item').on('click', () => {
    $('ul.my_list li:last').remove();
  });
  $('div#clear_list').on('click', () => {
    list.empty();
  });
}
);
