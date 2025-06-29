select
    project_id,
    employee_id
from
    (
    select
        p.project_id,
        p.employee_id,
        dense_rank() over(partition by p.project_id order by e.experience_years desc) as rnk
    from
        project p 
    join
        employee e 
    on
        p.employee_id = e.employee_id) as t
where
    t.rnk = 1;