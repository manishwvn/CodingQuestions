with cte as (select
    *,
    dense_rank() over(partition by customer_id order by order_date) as order_rank
from
    delivery)

select
    round(sum(case
        when order_date = customer_pref_delivery_date then 1 else 0
    end) / count(*) * 100, 2) as immediate_percentage
from
    cte
where
    order_rank = 1