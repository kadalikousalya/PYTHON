# Write your MySQL query statement below
SELECT name FROM SalesPerson 
WHERE sales_id not IN
(SELECT sales_id FROM Orders 
WHERE com_id=(SELECT com_id FROM Company
WHERE name='RED'))


