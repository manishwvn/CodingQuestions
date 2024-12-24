-- with order_counts as(
--     select
--         customer_id,
--         product_id,
--         count(*) as counts
--     from
--         orders o
--     group by
--         1,2
--     ),

-- order_freqs as (
--     select
--         *,
--         dense_rank() over(partition by customer_id order by counts desc) as freqs
--     from
--         order_counts
--     )

-- select 
--     f.customer_id,
--     f.product_id,
--     p.product_name
-- from
--     order_freqs f
-- join
--     products p
-- on
--     f.product_id = p.product_id
-- where 
--     freqs = 1;


with order_freqs as(
    select
        customer_id, 
        product_id,
        dense_rank() over(partition by customer_id order by count(product_id) desc) as most_frequent
    from
        orders
    group by
        customer_id, product_id
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
    most_frequent = 1;