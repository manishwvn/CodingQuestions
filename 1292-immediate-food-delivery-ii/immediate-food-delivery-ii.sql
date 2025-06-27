#intermediate approach
-- find 1st order date
-- keep only first orders
-- find immediate %

select
    round((sum(case
        when customer_pref_delivery_date = order_date then 1
        else 0
    end) / count(*)) * 100, 2) as immediate_percentage
from
    delivery
where (customer_id, order_date) in 
    (select
        customer_id,
        min(order_date) as first_order_date
    from
        delivery
    group by
        customer_id);