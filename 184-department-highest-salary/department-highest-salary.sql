WITH salaries_ranked AS (
    SELECT
        e.departmentId id,
        e.name name,
        e.salary salary,
        RANK() OVER(
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) srank
    FROM Employee e
)

SELECT
    d.name Department,
    sr.name Employee,
    sr.salary
FROM salaries_ranked sr
JOIN Department d ON d.id = sr.id
WHERE sr.srank = 1;

