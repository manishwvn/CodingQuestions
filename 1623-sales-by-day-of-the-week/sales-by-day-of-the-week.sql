select
    i.item_category as CATEGORY,
    sum(case when dayofweek(o.order_date) = 2 then o.quantity else 0 end) as MONDAY,
    sum(case when dayofweek(o.order_date) = 3 then o.quantity else 0 end) as TUESDAY,
    sum(case when dayofweek(o.order_date) = 4 then o.quantity else 0 end) as WEDNESDAY,
    sum(case when dayofweek(o.order_date) = 5 then o.quantity else 0 end) as THURSDAY,
    sum(case when dayofweek(o.order_date) = 6 then o.quantity else 0 end) as FRIDAY,
    sum(case when dayofweek(o.order_date) = 7 then o.quantity else 0 end) as SATURDAY,
    sum(case when dayofweek(o.order_date) = 1 then o.quantity else 0 end) as SUNDAY    
from
    items i
left join
    orders o
on
    i.item_id = o.item_id
group by
    i.item_category
order by
    1;