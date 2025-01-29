-- with cte as (
--     select
--         visited_on,
--         sum(amount) as daily_amount
--     from
--         customer
--     group by
--         visited_on),

-- cte2 as (select
--     *,
--     sum(daily_amount) over(order by visited_on range between interval 6 day preceding and current row) as rolling_sum,
--     avg(daily_amount) over(order by visited_on range between interval 6 day preceding and current row) as rolling_avg
-- from
--     cte)

-- select
--     visited_on,
--     rolling_sum as amount,
--     round(rolling_avg, 2) as average_amount
-- from
--     cte2
-- where
--     visited_on >= (select min(visited_on) + interval 6 day from customer)
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
cte2 as (
select 
    c1.visited_on as visited_on1,
    c1.daily_amount as amount1,
    c2.visited_on as visited_on2,
    c2.daily_amount as amount2
from 
    cte c1 
join 
    cte c2 
on 
    c1.visited_on >= c2.visited_on
where
    datediff(c1.visited_on, c2.visited_on) between 0 and 6
    and
    c1.visited_on >= (select min(visited_on) + interval 6 day from customer)
order by
    1, 3)

select
    visited_on1 as visited_on,
    sum(amount2) as amount,
    round(avg(amount2),2) as average_amount
from
    cte2
group by
    1
order by
    1;

