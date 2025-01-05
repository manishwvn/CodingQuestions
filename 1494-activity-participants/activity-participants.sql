with cte as (select
    activity,
    dense_rank() over(order by count(id)) as min_rnk,
    dense_rank() over(order by count(id) desc) as max_rnk
from
    friends
group by
    activity)

select
    activity
from
    cte
where
    min_rnk <> 1 and max_rnk <> 1;