-- with cte as (select
--     activity,
--     dense_rank() over(order by count(id)) as min_rnk,
--     dense_rank() over(order by count(id) desc) as max_rnk
-- from
--     friends
-- group by
--     activity)

-- select
--     activity
-- from
--     cte
-- where
--     min_rnk <> 1 and max_rnk <> 1;

with cte as (
select
    activity,
    count(id) as counts
from
    friends
group by
    activity),

cte2 as (
    select max(counts) as counts from cte
    union
    select min(counts) as counts from cte
)

select
    activity
from
    cte c1
left join
    cte2 c2
on
    c1.counts = c2.counts
where
    c2.counts is null;