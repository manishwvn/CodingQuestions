with cte as (
    select
        *,
        dense_rank() over(partition by city_id order by degree desc) as max_temp
    from
        weather)

select
    city_id,
    min(day) as day,
    degree
from
    cte
where
    max_temp = 1
group by
    city_id;