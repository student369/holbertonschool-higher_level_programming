-- Get the genres for the show Dexter
SELECT tvg.name FROM tv_genres AS tvg
       LEFT JOIN tv_show_genres AS tvsg
       ON tvsg.genre_id=tvg.id
       LEFT JOIN tv_shows AS tv
       ON tvsg.show_id=tv.id
       WHERE tv.title="Dexter"
       ORDER BY tvg.name;
