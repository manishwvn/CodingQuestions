select 
    transaction_id
from (
    select 
        -- date(day) as day, 
        transaction_id, 
        amount, 
        dense_rank() over (partition by date(day) order by amount desc) rk
    from Transactions
    ) t1
where 
    rk=1
order by 
    1; 