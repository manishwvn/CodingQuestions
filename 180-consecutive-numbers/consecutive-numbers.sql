with cte as (select
    *,
    lead(num, 1) over() as next_1,
    lead(num, 2) over() as next_2
from
    logs)

select
    distinct num as ConsecutiveNums
from
    cte
where
    num = next_1
    and
    num = next_2