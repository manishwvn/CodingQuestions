select
    c.name as country
from
    country c 
join
    person p 
on
    c.country_code = substr(p.phone_number, 1, 3)
join
    calls c1 
on
    p.id = c1.caller_id or p.id = c1.callee_id
group by 
    country
having
    avg(c1.duration) > (select avg(duration) from calls)