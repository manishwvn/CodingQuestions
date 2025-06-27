with cte as (
    select
        employee_id,
        count(department_id) as num_dept
    from
        employee 
    group by
        employee_id
)

select
    e.employee_id,
    e.department_id
from
    employee e
join
    cte c 
on
    e.employee_id = c.employee_id
where
    c.num_dept = 1
    or (c.num_dept > 1 and e.primary_flag = 'Y');