with cte as (select
    o.customer_id,
    c.name,
    month(o.order_date) as `month`,
    sum(o.quantity * p.price) as amount
from
    orders o
join
    product p 
on
    o.product_id = p.product_id
join
    customers c 
on
    o.customer_id = c.customer_id
where
    year(order_date) = 2020
    and
    (month(order_date) = 6 or month(order_date) = 7)
group by
    o.customer_id, month
having
    amount >= 100)

select
    customer_id, name
from
    cte
group by
    customer_id, name
having
    count(*) = 2