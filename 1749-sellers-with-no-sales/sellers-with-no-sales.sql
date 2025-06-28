with cte as (
    select
        *
    from
        orders
    where
        year(sale_date) = 2020)

select
    s.seller_name
from
    seller s
left join
    cte c
on
    s.seller_id = c.seller_id
where
    c.order_id is null
order by
    s.seller_name;