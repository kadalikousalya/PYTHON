# Write your MySQL query statement below
SELECT d.name AS Department,
e.name AS Employee,
e.salary AS salary
FROM Employee e
JOIN
Department d
ON e.departmentId=d.id

WHERE 3>(
    SELECT COUNT(DISTINCT (Salary))
    FROM Employee e2
    WHERE e2.Salary>e.salary AND
    e.DepartmentId=e2.DepartmentId
)

