-- Write your PostgreSQL query statement below
WITH manager_reports AS (
    SELECT managerID, COUNT(id) AS direct_reports
    FROM employee
    GROUP BY managerID
)
SELECT name
FROM employee
WHERE id IN (SELECT managerID 
             FROM manager_reports
             WHERE direct_reports >= 5);