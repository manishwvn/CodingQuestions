with order_counts as(
    select
        customer_id,
        product_id,
        count(*) as counts
    from
        orders o
    group by
        1,2
    ),

order_freqs as (
    select
        *,
        dense_rank() over(partition by customer_id order by counts desc) as freqs
    from
        order_counts
    )

select 
    f.customer_id,
    f.product_id,
    p.product_name
from
    order_freqs f
join
    products p
on
    f.product_id = p.product_id
where 
    freqs = 1;
