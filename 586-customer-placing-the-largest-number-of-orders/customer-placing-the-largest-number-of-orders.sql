with order_counts as (
    select
        customer_number,
        count(*) as orders
    from
        orders
    group by
        customer_number
)
select
    customer_number
from
    order_counts
where
    orders = (select max(orders) from order_counts);