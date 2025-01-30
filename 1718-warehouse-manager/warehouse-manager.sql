select
    w.name as warehouse_name,
    sum(p.width * p.height * p.length * w.units) as volume
from
    warehouse w
join
    products p
on
    p.product_id = w.product_id
group by
    w.name