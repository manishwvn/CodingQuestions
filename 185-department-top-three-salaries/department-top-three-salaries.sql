WITH E AS (SELECT
        DEPARTMENTID,
        NAME, 
        SALARY,
        DENSE_RANK() OVER(PARTITION BY DEPARTMENTID ORDER BY SALARY DESC) AS RNK
     FROM 
        EMPLOYEE

)


SELECT
    D.NAME AS 'Department',
    E.NAME AS 'Employee',
    E.SALARY AS 'Salary'
    
FROM
    E

JOIN
    DEPARTMENT D
ON 
    E.DEPARTMENTID = D.ID

WHERE
    RNK <= 3;
    
    
# SELECT
#     d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
# FROM
#     Employee e1
#         JOIN
#     Department d ON e1.DepartmentId = d.Id
# WHERE
#     3 > (SELECT
#             COUNT(DISTINCT e2.Salary)
#         FROM
#             Employee e2
#         WHERE
#             e2.Salary > e1.Salary
#                 AND e1.DepartmentId = e2.DepartmentId
#         )
# ;