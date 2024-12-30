with data1 as( 
    SELECT 
        a.customer_id, 
        a.transaction_date 
    FROM 
        Transactions a, 
        Transactions b 
    WHERE 
        a.customer_id = b.customer_id 
        AND b.amount > a.amount 
        AND DATEDIFF(b.transaction_date, a.transaction_date) = 1),

data2 as(
    select
        customer_id,
        transaction_date,
        row_number() over(partition by customer_id order by transaction_date) as rnk
    from
        data1
),

data3 as (
    select
        customer_id,
        transaction_date,
        date_sub(transaction_date, interval rnk day) as dategroup
    from
        data2
),

data4 as (
    select
        customer_id,
        min(transaction_date) as consecutive_start,
        count(*) as cnt
    from
        data3
    group by
        customer_id, dategroup)

select
    customer_id,
    consecutive_start,
    date_add(consecutive_start, interval cnt day) as consecutive_end
from
    data4
where
    cnt > 1
order by
    customer_id;