select
    department as Department,
    name as Employee,
    salary as Salary 
from
    (select
        e.*, d.name as department, 
        dense_rank() over(partition by d.id order by e.salary desc) as rnk
    from
        department d 
    join
        employee e 
    on
        d.id = e.departmentId
    ) t
where
    t.rnk <=3;


