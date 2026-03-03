SELECT g.name AS genre, COUNT(sg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
