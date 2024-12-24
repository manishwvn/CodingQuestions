select
    c.name as Customers
from
    Customers c
left join
    orders o
on
    c.id = o.customerid
where
    o.id is null;