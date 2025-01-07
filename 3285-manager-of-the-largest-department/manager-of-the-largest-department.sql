with cte as (
select
    e1.emp_name as manager_name,
    e1.dep_id,
    count(e2.emp_id) as counts
from
    employees e1
join
    employees e2
on
    e1.dep_id = e2.dep_id
where
    e1.position = 'Manager'
group by
    e1.dep_id),

cte2 as (
select
    *,
    dense_rank() over(order by counts desc) as rnk
from
    cte)

select manager_name, dep_id from cte2 where rnk = 1 order by dep_id;