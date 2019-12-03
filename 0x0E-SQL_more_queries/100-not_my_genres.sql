-- Get the Dexter's genres
SELECT tvg.name as name FROM tv_shows AS tv
       INNER JOIN tv_show_genres AS tvsg
       ON tvsg.show_id=tv.id
       AND tv.title="Dexter"
       RIGHT JOIN tv_genres AS tvg
       ON tvsg.genre_id=tvg.id
       WHERE tvsg.genre_id IS NULL ORDER BY name;
