select
    s.user_id,
    sum(p.price * s.quantity) as spending
from
    sales s
join
    product p
on
    s.product_id = p.product_id
group by
    s.user_id
order by
    2 desc, 1 asc;