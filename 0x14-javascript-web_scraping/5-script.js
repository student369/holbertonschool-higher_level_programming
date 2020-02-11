const $ = window.$;
$('div#add_item').click(function (event) {
  $('ul.my_list').append(' <li>Item</li>');
});
