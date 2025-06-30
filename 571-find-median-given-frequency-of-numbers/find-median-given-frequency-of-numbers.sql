with recursive cte as (
    select
        1 as freq
    union all
    select
        freq + 1
    from
        cte
    where
        freq < (select max(frequency) from numbers)
),

nums as (select
    n.num
from
    numbers n
left join
    cte c
on
    n.frequency >= c.freq),

num_ranks as (select
    num,
    row_number() over(order by num) as rnk,
    count(num) over() as total
from
    nums),

median_rnks as (select
    *,
    case
        when total % 2 = 0  then rnk in (total/ 2, (total/2)+1)
        else rnk = (total+1) / 2 
    end as consider
from
    num_ranks)

select
    round(avg(num), 1) as median
from
    median_rnks
where
    consider = 1