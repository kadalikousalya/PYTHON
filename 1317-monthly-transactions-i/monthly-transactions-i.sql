# Write your MySQL query statement below
SELECT 
DATE_FORMAT(trans_date,'%Y-%m') AS 'month',
country,
COUNT(*) as trans_count,
SUM(state='approved') AS approved_count,
SUM(amount) as trans_total_amount,
SUM(CASE WHEN state='approved' THEN amount
ELSE 0 END) as approved_total_amount
FROM Transactions
GROUP BY month,country