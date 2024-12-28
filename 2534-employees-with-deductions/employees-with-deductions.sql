with cte as (select
    employee_id,
    sum(ceil(timestampdiff(second, in_time, out_time) / 60)) total_time
from
    logs
group by
    employee_id)

select
    e.employee_id
from
    employees e
left join
    cte c
on
    e.employee_id = c.employee_id
where
    e.needed_hours * 60 > ifnull(c.total_time, 0)

