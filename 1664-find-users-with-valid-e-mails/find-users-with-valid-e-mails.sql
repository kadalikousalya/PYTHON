# Write your MySQL query statement be
SELECT user_id,name,mail
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode(\\?com)?\\.com$';