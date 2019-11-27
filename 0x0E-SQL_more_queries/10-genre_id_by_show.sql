-- Get the cities and display state information
SELECT tv.title, tvsg.genre_id FROM tv_shows AS tv
       RIGHT JOIN tv_show_genres AS tvsg ON tv.id = tvsg.show_id
       ORDER BY tv.title, tvsg.genre_id ASC;
