select
    project_id
from
    (
select
    project_id,
    dense_rank() over(order by count(employee_id) desc) as rnk
from
    project p
group by
    project_id) t
where
    t.rnk = 1;