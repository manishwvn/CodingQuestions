-- -- select
-- --     w1.id as Id
-- -- from
-- --     Weather w1
-- -- left join
-- --     Weather w2
-- -- on
-- --     w2.recordDate = w1.recordDate - INTERVAL 1 DAY
-- -- where
-- --     w1.temperature > w2.temperature;
-- with cte as (
-- select
--     *,
--     LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
--     lag(temperature) over(order by recorddate) as prev
-- from
--     weather)

-- select
--     id
-- from
--     cte
-- where
--     temperature > prev
--     and
--     recorddate = date_add(prev_date, interval 1 day)

with cte as (
select
    *,
    lag(recordDate) over(order by recordDate) as prev_date,
    lag(temperature) over(order by recordDate) as prev_temp
from
    weather)

select
    id
from
    cte
where
    prev_date = recordDate - interval 1 day
    and
    temperature > prev_temp;