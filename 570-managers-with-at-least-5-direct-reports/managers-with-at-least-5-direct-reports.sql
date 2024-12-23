select
    e1.name
from
    employee e1
join
    employee e2
on
    e1.id = e2.managerid
group by
    e1.name, e1.id
having
    count(*) >= 5;