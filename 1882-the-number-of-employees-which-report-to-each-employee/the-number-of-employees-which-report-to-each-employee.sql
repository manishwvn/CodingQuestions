select
    e.employee_id,
    e.name,
    count(e.employee_id) as reports_count,
    round(avg(r.age)) as average_age
from
    employees e
left join
    employees r
on
    e.employee_id = r.reports_to
where
    r.reports_to is not null
group by
    e.employee_id, e.name
order by
    1;