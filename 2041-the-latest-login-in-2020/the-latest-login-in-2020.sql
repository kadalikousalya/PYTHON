# Write your MySQL query statement below
SELECT (user_id),max(time_stamp) as last_stamp 
FROM Logins
WHERE time_stamp>'2020-01-01' AND time_stamp<'2021-01-01'
GROUP BY user_id
