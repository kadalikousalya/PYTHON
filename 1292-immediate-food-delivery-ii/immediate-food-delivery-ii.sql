# Write your MySQL query statement below

SELECT 
ROUND(
    SUM(order_date=customer_pref_delivery_date)*100.00/COUNT(*),2
) AS immediate_percentage
FROM
Delivery d
JOIN
(SELECT customer_id,MIN(order_date) as first_date
FROM Delivery
GROUP BY customer_id)
AS first
ON d.customer_id=first.customer_id AND first.first_date=d.order_date