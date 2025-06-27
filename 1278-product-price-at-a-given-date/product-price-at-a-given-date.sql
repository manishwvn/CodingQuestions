with cte as (
    select
        *,
        dense_rank() over(partition by product_id order by change_date desc) as rnk
    from
        products
    where
        change_date <= date('2019-08-16')
)

select
    p.product_id,
    coalesce(c.new_price, 10) as price 
from
    products p
left join
    cte c
on
    p.product_id = c.product_id
    and
    c.rnk = 1
group by
    p.product_id;