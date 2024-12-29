with cte as (
    select
        s.user_id,
        s.product_id,
        sum(s.quantity * p.price) as amount
    from
        sales s
    left join
        product p
    on
        s.product_id = p.product_id
    group by 1, 2),

cte2 as (
    select
        *,
        max(amount) over(partition by user_id) as max_spent
    from
        cte
)

select
    user_id,
    product_id
from
    cte2
where
    amount = max_spent