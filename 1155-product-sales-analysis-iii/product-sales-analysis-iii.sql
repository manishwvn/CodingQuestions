with first_years as (
    select
        product_id,
        min(year) as first_year
    from
        Sales
        group by product_id
)

select
    s.product_id,
    s.year as first_year,
    s.quantity,
    s.price
from
    Sales s
join
    first_years f
on
    s.product_id = f.product_id and s.year = f.first_year;