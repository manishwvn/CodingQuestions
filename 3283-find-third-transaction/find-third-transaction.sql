with cte as (select
    *,
    rank() over(partition by user_id order by transaction_date) as trans_rnk
from
    transactions),

cte2 as (
    select
        *,
        rank() over(partition by user_id order by spend) as spend_rnk
    from
        cte
    where
        trans_rnk <= 3
)

select
    user_id, 
    spend as third_transaction_spend, 
    transaction_date as third_transaction_date
from
    cte2
where
    trans_rnk = 3
    and
    spend_rnk = 3;