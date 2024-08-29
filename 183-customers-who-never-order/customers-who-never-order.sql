select
    c.name as customers
from
    Customers c
left join
    Orders o
on
    c.id = o.customerid
where
    o.customerid is NULL;