with cte as (select
    *,
    dense_rank() over(partition by player_id order by event_date) as rnk,
    lead(event_date,1) over(partition by player_id order by event_date) as nxt_login
from
    activity)

select
    event_date as install_dt,
    count(*) as installs,
    round(sum(case when
        datediff(nxt_login, event_date) = 1 then 1 
    else 0 end) / count(*), 2) as Day1_retention
from
    cte
where
    rnk = 1
group by
    event_date