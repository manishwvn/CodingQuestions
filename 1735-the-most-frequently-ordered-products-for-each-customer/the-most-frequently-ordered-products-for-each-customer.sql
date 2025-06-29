with cte as (
select
    o.customer_id,
    o.product_id,
    p.product_name,
    dense_rank() over(partition by customer_id order by count(o.product_id) desc) as rnk
from
    orders o 
join
    products p 
on
    o.product_id = p.product_id
group by
    o.customer_id, o.product_id)

select
    customer_id,
    product_id,
    product_name
from
    cte
where rnk = 1;