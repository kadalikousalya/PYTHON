# Write your MySQL query statement below


SELECT 'Low Salary' as category ,count(account_id) as accounts_count
FROM Accounts where income<20000
union
SELECT 'Average Salary' as category,count(account_id) as accounts_count
from Accounts where income between 20000 and 50000
union
select 'High Salary' as category ,count(account_id) as accounts_count
from Accounts where income>50000