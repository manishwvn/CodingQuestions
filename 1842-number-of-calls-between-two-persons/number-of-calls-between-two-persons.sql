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


-- SELECT 
--     LEAST(from_id, to_id) AS person1, 
--     GREATEST(from_id, to_id) AS person2, 
--     COUNT(*) AS call_count, 
--     SUM(duration) AS total_duration
-- FROM Calls
-- GROUP BY 1, 2