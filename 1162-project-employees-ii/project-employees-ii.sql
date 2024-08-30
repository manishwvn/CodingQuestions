WITH EmployeeCount AS (
    SELECT project_id, COUNT(employee_id) AS employee_count
    FROM Project
    GROUP BY project_id
)
SELECT project_id
FROM EmployeeCount
WHERE employee_count = (SELECT MAX(employee_count) FROM EmployeeCount);