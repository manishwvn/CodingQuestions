with cte as (select
    num,
    id - row_number() over(partition by num order by id) as grouped
from
    logs)

select
    distinct num as ConsecutiveNums
from
    cte
group by
    num, grouped
having
    count(*) >= 3;

-- select * from cte2