with cte as (
    select
        p1.product_id as product1_id,
        p2.product_id as product2_id,
        p1.category as product1_category,
        p2.category as product2_category
    from
        productinfo p1
    join
        productinfo p2
    on
        p1.product_id < p2.product_id
)

select
    c.product1_id,
    c.product2_id,
    c.product1_category,
    c.product2_category,
    count(*) as customer_count
from
    cte c
join
    ProductPurchases p1
on
    p1.product_id = c.product1_id
join
    ProductPurchases p2
on
    p2.product_id = c.product2_id
where
    p1.user_id = p2.user_id
group by
    1,2,3,4
having
    customer_count >= 3
order by
    5 desc, 1 asc, 2 asc;