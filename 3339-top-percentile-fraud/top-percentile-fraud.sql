select
    policy_id,
    state,
    fraud_score
from
    (
    select
        *,
        rank() over(partition by state order by fraud_score desc) as rnk
    from
        fraud) t
where
    rnk = 1
order by state, fraud_score desc, policy_id asc;