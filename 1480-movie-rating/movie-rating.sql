# Write your MySQL query statement below

(SELECT u.name AS results
FROM users u
JOIN Movierating mr
ON u.user_id=mr.user_id
GROUP BY u.name,u.user_id
ORDER BY COUNT(*) DESC,u.name
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM Movies m 
JOIN Movierating mr
ON m.movie_id=mr.movie_id
WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-28'
GROUP BY m.movie_id 
ORDER BY AVG(rating) DESC,m.title
LIMIT 1)


