-- Get the shows with a name of the genres
SELECT tv.title, tvg.name FROM tv_shows AS tv
       LEFT JOIN tv_show_genres AS tvsg
       ON tvsg.show_id=tv.id
       LEFT JOIN tv_genres AS tvg
       ON tvsg.genre_id=tvg.id
       ORDER BY tv.title, tvg.name ASC;
