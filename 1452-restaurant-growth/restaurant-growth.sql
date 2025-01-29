-- with cte as (select
--     visited_on,
--     sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as rolling_sum,
--     avg(amount) over(order by visited_on range between interval 6 day preceding and current row) as rolling_avg
-- from
--     customer
-- group by
--     visited_on)

-- select
--     visited_on,
--     rolling_sum as amount,
--     round(rolling_avg,2) as average_amount
-- from
--     cte
-- where
--     visited_on >= (select min(visited_on) + interval 6 day as visited_on from customer)
-- order by
--     visited_on;

with cte as (
    select
        visited_on,
        sum(amount) as daily_amount
    from
        customer
    group by
        visited_on),

cte2 as (select
    *,
    sum(daily_amount) over(order by visited_on range between interval 6 day preceding and current row) as rolling_sum,
    avg(daily_amount) over(order by visited_on range between interval 6 day preceding and current row) as rolling_avg
from
    cte)

select
    visited_on,
    rolling_sum as amount,
    round(rolling_avg, 2) as average_amount
from
    cte2
where
    visited_on >= (select min(visited_on) + interval 6 day from customer)
order by
    visited_on;