select
    c.country_name,
    case
        when avg(w.weather_state) <= 15 then 'Cold'
        when avg(w.weather_state) >= 25 then 'Hot'
        else 'Warm'
    end as weather_type
from
    countries c
join
    weather w
on
    c.country_id = w.country_id
and
    month(day) = '11' and year(day) = '2019'
group by
    c.country_name;