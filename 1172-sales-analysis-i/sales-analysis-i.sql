select t.seller_id from(
    select
    s.seller_id,
    dense_rank() over( order by sum(s.price) desc) as rnk
from
    sales s
join
    product p
on
    s.product_id = p.product_id
group by
    s.seller_id) as t
where t.rnk = 1;