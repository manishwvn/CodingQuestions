with cte as (
    select
        o.order_id,
        o.order_date,
        o.product_id,
        p.product_name,
        dense_rank() over(partition by o.product_id order by o.order_date desc) as rnk
    from
        orders o
    left join
        products p
    on
        o.product_id = p.product_id)

select
    product_name,
    product_id,
    order_id,
    order_date
from
    cte
where
    rnk = 1
order by
    1,2,3