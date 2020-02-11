const $ = window.$;
$.get('https://swapi.co/api/films/?format=json', function (data) {
  const dataResult = data.results;
  for (let i = 0; i < data.count; i++) {
    $('UL#list_movies').append('<li>' + dataResult[i].title + '</li>');
  }
});
