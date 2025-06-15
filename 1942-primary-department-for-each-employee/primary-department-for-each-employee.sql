# Write your MySQL query statement below
SELECT employee_id,department_id
FROM Employee
WHERE primary_flag='Y'
or
employee_id IN (
SELECT employee_id
FROM EMPLOYEE
GROUP BY employee_id
HAVING COUNT(employee_id)=1)
