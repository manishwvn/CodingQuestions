with cte as (
    select
        customer_number,
        count(customer_number) as counts,
        dense_rank() over(order by count(customer_number) desc) as rnk 
    from
        orders
    group by
        customer_number
)

select
    customer_number
from
    cte
where
    rnk = 1;