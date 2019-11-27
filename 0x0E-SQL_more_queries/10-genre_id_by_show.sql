-- Get the cities and display state information
SELECT tv.title, tvg.genre_id FROM tv_shows as tv
       RIGHT JOIN tv_show_genres as tvg ON tv.id = tvg.show_id
       ORDER BY tv.title, tvg.genre_id;
