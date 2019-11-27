-- Get the count of shows by genre
SELECT tvg.name AS genre, COUNT(tvsg.genre_id) AS number_of_shows
       FROM tv_show_genres AS tvsg LEFT JOIN tv_genres AS tvg
       ON tvsg.genre_id=tvg.id
       GROUP BY genre HAVING number_of_shows > 0
       ORDER BY number_of_shows DESC;
