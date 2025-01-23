with cte as (
    select
        o.*,
        c.customer_name
    from
        orders o
    left join
        customers c
    on
        o.customer_id = c.customer_id),

cte2 as (
    select
        customer_id,
        customer_name,
        group_concat(distinct product_name order by product_name) as products
    from
        cte
    group by
        customer_id
    having
        products like 'A,B%'
        and
        products not like '%C%')

select
    customer_id,
    customer_name
from
    cte2;