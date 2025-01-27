with cte as (select
    num,
    row_number() over(order by id) as rn_id,
    row_number() over(partition by num order by id) as rn_num
from
    logs),

cte2 as (
    select
        num,
        rn_id - rn_num as grouped
    from
        cte
)

select
    distinct num as ConsecutiveNums
from
    cte2
group by
    num, grouped
having
    count(*) >= 3;