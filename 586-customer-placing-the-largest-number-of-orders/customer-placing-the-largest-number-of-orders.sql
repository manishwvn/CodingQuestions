with order_counts as (
    select
        customer_number,
        count(*) as orders
    from
        orders
    group by
        customer_number
),
max_order_count as (
    select
        max(orders) as max_orders
    from
        order_counts
)
select
    customer_number
from
    order_counts
where
    orders = (select max_orders from max_order_count);