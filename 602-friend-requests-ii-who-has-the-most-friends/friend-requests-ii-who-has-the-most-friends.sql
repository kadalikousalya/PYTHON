# Write your MySQL query statement below
WITH CTE AS(
    SELECT requester_id AS id,
    COUNT(requester_id) AS ctn
    FROM RequestAccepted 
    GROUP BY requester_id


    UNION ALL

    SELECT accepter_id AS id,
    COUNT(accepter_id) AS ctn
    FROM RequestAccepted
    GROUP BY accepter_id 
)

SELECT id,
sum(ctn) AS num
FROM CTE
group by id
ORDER BY num DESC
LIMIT 1