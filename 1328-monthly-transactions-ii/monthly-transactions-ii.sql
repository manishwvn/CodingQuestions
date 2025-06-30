with chargebacks_cte as (
    select 
        DATE_FORMAT(chargebacks.trans_date, '%Y-%m') AS month,
        country,
        'back' as state, 
        amount 
    from 
        chargebacks 
    join 
        transactions 
    on 
        chargebacks.trans_id = transactions.id 
),
transactions_cte as (
    select 
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        'approved' as state, 
        amount 
    from 
        transactions
    where 
        state = 'approved'
)
select 
    month, 
    country, 
    sum(case when state = 'approved' then 1 else 0 end) as approved_count, 
    sum(case when state = 'approved' then amount else 0 end) as approved_amount, 
    sum(case when state = 'back' then 1 else 0 end) as chargeback_count, 
    sum(case when state = 'back' then amount else 0 end) as chargeback_amount
from 
    (
        select month, country, state, amount from chargebacks_cte
        union all 
        select month, country, state, amount from transactions_cte
    ) tmp
group by 
    1, 2