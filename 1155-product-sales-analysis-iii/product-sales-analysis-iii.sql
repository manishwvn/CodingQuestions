select
    s1.product_id,
    s1.year as first_year,
    s1.quantity,
    s1.price
from
    sales s1
join
    (select
        product_id, min(year) as first_year
    from
        sales
    group by
        product_id) s2
on
    s1.product_id = s2.product_id
    and
    s1.year = s2.first_year
order by
    s1.product_id;