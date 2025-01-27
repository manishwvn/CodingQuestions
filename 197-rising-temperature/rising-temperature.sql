with cte as (
    select
        *,
        lag(recordDate) over(order by recordDate) as prevDate,
        lag(temperature) over(order by recordDate) as prevTemp
    from
        Weather
)

select
    id
from
    cte
where
    temperature > prevTemp
    and
    datediff(recordDate, prevDate) = 1;