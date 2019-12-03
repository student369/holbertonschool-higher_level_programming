-- Get the shows that don't have genre commedy
SELECT tv.title FROM tv_shows AS tv
       WHERE tv.id NOT IN
       (SELECT tv.id
       FROM tv_shows AS tv
       INNER JOIN tv_show_genres AS tvsg
       ON tv.id=tvsg.show_id
       INNER JOIN tv_genres AS g
       ON tvsg.genre_id=g.id
       WHERE g.name="Comedy")
       ORDER BY tv.title;
