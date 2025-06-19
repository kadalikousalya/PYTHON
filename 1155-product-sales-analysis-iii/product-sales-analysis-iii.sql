# Write your MySQL query statement below
SELECT s.product_id,s.year AS first_year ,s.quantity,s.price
FROM Sales s
JOIN 
(SELECT product_id,MIN(year) AS first_year1 FROM Sales
GROUP BY product_id) AS first_year
ON s.product_id=first_year.product_id AND s.year=first_year.first_year1;