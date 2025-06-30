with cte as (select
    city,
    hour(call_time) as hour,
    count(*) as call_count
from
    calls
group by
    city, hour),

cte2 as (
    select
        *,
        dense_rank() over(partition by city order by call_count desc) as rnk
    from
        cte
)

select
    city,
    hour as peak_calling_hour,
    call_count as number_of_calls
from
    cte2
where
    rnk = 1
order by
    2 desc, 1 desc;