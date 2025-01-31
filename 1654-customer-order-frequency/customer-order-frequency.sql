with cte as (SELECT
    o.customer_id,
    c.name,
    month(o.order_date) as month,
    sum(p.price * o.quantity) as total
FROM
    orders o
LEFT JOIN
    customers c ON o.customer_id = c.customer_id
LEFT JOIN
    product p ON o.product_id = p.product_id
WHERE
    YEAR(o.order_date) = 2020
    AND (MONTH(o.order_date) = 6 OR MONTH(o.order_date) = 7)
group by
    c.customer_id, month
having
    sum(p.price * o.quantity) >= 100)

select
    customer_id,
    name
from
    cte
group by
    customer_id, name
having
    count(*) = 2;