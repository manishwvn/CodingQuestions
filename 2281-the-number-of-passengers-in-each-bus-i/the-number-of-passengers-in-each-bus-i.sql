with used_bus as (select passenger_id, min(b.arrival_time) as m
			from passengers p join buses b 
			on p.arrival_time <= b.arrival_time
			group by passenger_id)


select 
    bus_id, count(used_bus.m) as passengers_cnt
from 
    buses 
left join 
    used_bus 
on 
    (used_bus.m = buses.arrival_time)
group by 
    bus_id
order by
    bus_id
