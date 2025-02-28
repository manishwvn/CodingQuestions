select
    bike_number,
    max(end_time) as end_time
from
    bikes
group by
    bike_number
order by
    end_time desc;