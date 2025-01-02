with max_exp as (
    select
        p.project_id,
        e.employee_id,
        rank() over(partition by p.project_id order by experience_years desc) as rnk
    from
        project p
    join
        employee e
    on
        p.employee_id = e.employee_id)

select
    project_id,
    employee_id
from
    max_exp
where
    rnk = 1;