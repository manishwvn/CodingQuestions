-- SELECT 
--     A.NAME AS 'EMPLOYEE'
-- FROM
--     EMPLOYEE AS A,
--     EMPLOYEE AS B
-- WHERE
--     A.MANAGERID = B.ID
--     AND
--     A.SALARY > B.SALARY;

select
    a.name as Employee
from
    employee a
join
    employee b
on
    a.managerid = b.id
where
    a.salary > b.salary;