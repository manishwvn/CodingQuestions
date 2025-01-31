with cte as (select
    from_id as person1,
    to_id as person2,
    duration
from
    calls
union all
select
    to_id,
    from_id,
    duration
from
    calls)

select
    person1,
    person2,
    count(*) as call_count,
    sum(duration) as total_duration
from
    cte
where
    person1 < person2
group by
    person1, person2;