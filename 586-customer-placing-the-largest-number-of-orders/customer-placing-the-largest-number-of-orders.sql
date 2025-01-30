with cte as (select
    customer_number,
    dense_rank() over(order by count(*) desc) as rnk
from
    orders
group by
    customer_number)

select
    customer_number
from
    cte
where
    rnk = 1;