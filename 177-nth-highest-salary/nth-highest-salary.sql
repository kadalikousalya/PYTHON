CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE
offset_value INT;
SET offset_value=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT SALARY
      FROM EMPLOYEE
      ORDER BY SALARY DESC
      LIMIT 1 OFFSET offset_value
  );
END