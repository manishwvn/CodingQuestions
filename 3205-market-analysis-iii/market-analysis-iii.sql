with cte as (
    select
        o.*,
        u.favorite_brand,
        i.item_brand
    from
        orders o
    left join
        users u
    on
        o.seller_id = u.seller_id
    left join
        items i
    on
        o.item_id = i.item_id
    where
        i.item_brand <> u.favorite_brand),
cte2 as (
    select
        seller_id,
        count(distinct item_id) as num_items,
        dense_rank() over(order by count(distinct item_id) desc) as rnk
    from
        cte
    group by
        seller_id
    order by
        seller_id)

select
    seller_id,
    num_items
from
    cte2
where
    rnk = 1;