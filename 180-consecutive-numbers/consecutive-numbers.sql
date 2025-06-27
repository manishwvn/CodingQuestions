with cte as (select
    *,
    row_number() over(partition by num order by id) as rnk
from
    logs),

 cte2 as (select
    *,
    id - rnk as grp
from
    cte)

select
    distinct num as ConsecutiveNums
from
    cte2
group by
    num, grp
having
    count(id) >= 3;