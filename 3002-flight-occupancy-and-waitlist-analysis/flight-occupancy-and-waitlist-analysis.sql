with cte as (select
    f.*,
    p.passenger_id,
    count(passenger_id) over(partition by flight_id) as p_count
from
    flights f
left join
    passengers p
on
    f.flight_id = p.flight_id)

select
    flight_id,
    case
        when
            p_count <= capacity then p_count
        else
            capacity
    end as booked_cnt,
    case
        when
            p_count > capacity then p_count - capacity
        else
            0
    end as waitlist_cnt
from
    cte
group by
    flight_id
order by
    flight_id asc;