with cte as (select
    *,
    avg(occurrences) as avg
from
    events
group by
    event_type)

select
    e.business_id
from
    events e
join
    cte c
on
    e.event_type = c.event_type
and
    e.occurrences > c.avg
group by
    e.business_id
having
    count(e.business_id) > 1
