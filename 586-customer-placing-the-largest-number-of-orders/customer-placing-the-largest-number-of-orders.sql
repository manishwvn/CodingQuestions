select
    customer_number
    -- count(customer_number) as counts
from
    orders
group by
    1
order by
    count(customer_number) desc
limit 1;