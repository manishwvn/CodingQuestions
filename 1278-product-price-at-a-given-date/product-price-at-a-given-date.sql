
with upd_prices as (
    select
        *,
        dense_rank() over(partition by product_id order by change_date desc) rnk
    from
        products
    where
        change_date <= date('2019-08-16'))

select
    product_id,
    new_price as price
from
    upd_prices
where
    rnk = 1
union
select
    product_id,
    10 as price
from
    products
where
    product_id not in (
        select product_id from upd_prices
    );