with prod_volumes as (
    select
        product_id,
        (width * length * height) as prod_volume
    from
        products
)

select
    w.name as warehouse_name,
    sum(p.prod_volume * w.units) as volume
from
    warehouse w
join
    prod_volumes p
on
    p.product_id = w.product_id
group by
    w.name