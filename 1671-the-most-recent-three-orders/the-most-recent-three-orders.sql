with order_ranks as(
    select
        c.name as customer_name,
        o.customer_id,
        o.order_id,
        o.order_date,
        dense_rank() over(partition by o.customer_id order by o.order_date desc) as rnk
    from
        orders o
    left join
        customers c
    on
        o.customer_id = c.customer_id
    )

select
    customer_name,
    customer_id,
    order_id,
    order_date
from
    order_ranks
where
    rnk <= 3
order by 1, 2, 4 desc;