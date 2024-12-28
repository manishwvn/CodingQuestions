with cte as(
    select
        product_id,
        year(purchase_date),
        count(*),
        year(purchase_date) - row_number() over(partition by product_id order by year(purchase_date)) as diff
    from
        orders
    group by product_id, year(purchase_date)
    having count(*) >= 3)

select
    distinct
    product_id
from
    cte
group by
    product_id, diff
having
    count(*) >= 2