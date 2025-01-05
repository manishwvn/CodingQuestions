with cte as (
    select
        *,
        row_number() over(partition by company order by salary) as rnk,
        count(*) over(partition by company) as counts
    from
        employee)

select
    id, company, salary
from
    cte
where
    rnk between (counts/2) and (counts/2) + 1;