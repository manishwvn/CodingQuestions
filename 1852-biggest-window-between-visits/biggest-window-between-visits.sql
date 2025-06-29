with cte as (select
    *,
    lead(visit_date) over(partition by user_id order by visit_date) as next_date
from
    uservisits),

cte2 as(
select
    user_id,
    -- case
    --     when next_date is null then datediff(date('2021-01-01'), visit_date)
    --     else datediff(next_date, visit_date)
    -- end as windows

    datediff(coalesce(next_date, date('2021-01-01')), visit_date) as windows
from
    cte)

select
    user_id,
    max(windows) as biggest_window
from
    cte2
group by
    user_id
order by
    user_id;
