with cte as (select
    *,
    (seat_id) - row_number() over(order by seat_id) as diff
from
    cinema
where
    free = 1),

cte2 as (
    select
        seat_id,
        count(diff) over(partition by diff) as cnt
    from
        cte

)

select seat_id from cte2 where cnt > 1 order by seat_id;