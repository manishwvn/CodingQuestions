select customer_number
from (
    select
        customer_number,
        count(*) as orders,
        row_number() over (order by count(*) desc) as rnk
    from
        orders
    group by
        customer_number
) ranked_orders
where rnk = 1;