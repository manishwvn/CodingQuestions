#beginner approach
-- find 1st order date
-- keep only first orders
-- find immediate %

select
    round((sum(case
        when d1.customer_pref_delivery_date = d1.order_date then 1
        else 0
    end) / count(*)) * 100, 2) as immediate_percentage
from
    delivery d1
join
    (select
        customer_id,
        min(order_date) as first_order_date
    from
        delivery
    group by
        customer_id) as d2
on 
    d1.customer_id = d2.customer_id
    and
    d1.order_date = d2.first_order_date