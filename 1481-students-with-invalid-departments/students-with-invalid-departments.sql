with cte as (select
    distinct d.id
from
    departments d
join
    students s
on
    d.id = s.department_id)

select
    id, name
from
    students
where
    department_id not in (select id from cte)