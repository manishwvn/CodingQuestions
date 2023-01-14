SELECT 
    E1.EMPLOYEE_ID AS 'employee_id',
    E1.NAME AS 'name', 
    COUNT(E2.REPORTS_TO) AS 'reports_count', 
    ROUND(AVG(E2.AGE)) AS 'average_age'
    
FROM 
    EMPLOYEES E1
    INNER JOIN
    EMPLOYEES E2
    ON E1.EMPLOYEE_ID = E2.REPORTS_TO
    
GROUP BY 
    E1.EMPLOYEE_ID

ORDER BY
    E1.EMPLOYEE_ID;
    
    
    