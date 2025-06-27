with cte1 as (select
    *,
    datediff('2019-08-16', change_date) as diff 
from
    products),

cte2 as (select
    product_id,
    min(diff) as min_diff
from
    cte1
where
    diff >= 0
group by
    product_id)

select
    product_id,
    coalesce(sum(price), 10) as price
from
    (
select
    c1.*,
    c2.min_diff,
    case
        when c1.diff = c2.min_diff then new_price
        when c1.diff <> c2.min_diff then 0
        else null
    end as price
from
    cte1 c1 
left join
    cte2 c2 
on
    c1.product_id = c2.product_id) as t 
group by
    product_id