with cte as (
    select
        *,
        row_number() over(partition by id order by month desc) as rnk
    from
        employee)


select
    id,
    month,
    sum(salary) over(partition by id order by month range between 2 preceding and current row) as Salary
from
    cte
where rnk <> 1
order by
    id, month desc;