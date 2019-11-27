-- Get the titles by genre
SELECT tv.title, tvg.genre_id FROM tv_shows AS tv
       LEFT JOIN tv_show_genres AS tvg ON tv.id = tvg.show_id
       ORDER BY tv.title, tvg.genre_id;
