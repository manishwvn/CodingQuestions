with recursive cte2 as (select
        bus_id,
        capacity,
        (select count(1) from passengers p where p.arrival_time <= b.arrival_time) as cnts,
        row_number() over(order by arrival_time) as rn
    from
        buses b),

cte as (
    select rn, 
        bus_id, 
        capacity,
        cnts,
        least(capacity, cnts) as onboarded,
        least(capacity, cnts) as total_onboarded
    from
        cte2
    where rn = 1
    union all
    select
        c2.rn, 
        c2.bus_id,
        c2.capacity,
        c2.cnts,
        least(c2.capacity, c2.cnts - c1.total_onboarded) as onboarded,
        c1.total_onboarded + least(c2.capacity, c2.cnts - c1.total_onboarded) as total_onboarded
    from
        cte c1
    join
        cte2 c2
    on
        c2.rn = c1.rn + 1
)



select
    bus_id,
    onboarded as passengers_cnt
from
    cte
order by 1;
