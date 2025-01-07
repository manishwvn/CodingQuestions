select
    p.product_id,
    case
        when d.discount is not null then
            p.price - ((d.discount * p.price)/100)
        else
            p.price
        end as final_price,
    p.category
from
    products p
left join
    discounts d
on
    p.category = d.category
