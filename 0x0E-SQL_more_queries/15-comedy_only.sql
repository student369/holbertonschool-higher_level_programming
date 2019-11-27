-- Get the comedy shows
SELECT tv.title FROM tv_shows AS tv
       LEFT JOIN tv_show_genres AS tvsg
       ON tvsg.show_id=tv.id
       LEFT JOIN tv_genres AS tvg
       ON tvsg.genre_id=tvg.id
       WHERE tvg.name="Comedy"
       ORDER BY tv.title;
