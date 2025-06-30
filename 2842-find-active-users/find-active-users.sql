with cte as (
select
    *,
    lead(created_at) over(partition by user_id order by created_at) as next_date
from
    users)

select
    distinct user_id
from
    cte
where
    datediff(next_date, created_at) <= 7