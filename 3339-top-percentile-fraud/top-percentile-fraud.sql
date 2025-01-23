with cte as (select
    *,
    rank() over(partition by state order by fraud_score desc) as rnk,
    count(*) over(partition by state) as state_count
from
    fraud)

select
    policy_id,
    state,
    fraud_score
from
    cte
where
    rnk <= ceil(state_count * 0.05)
order by
    state,
    fraud_score desc,
    policy_id;