-- with daily_sales as(
--     select
--         visited_on,
--         sum(amount) as daily_amount
--     from
--         customer
--     group by
--         visited_on
-- ),
-- moving_sales as(
--     select
--         visited_on,
--         sum(daily_amount) over(order by visited_on rows between 6 preceding and current row) as week_amount,
--         count(distinct daily_amount) over(order by visited_on rows between 6 preceding and current row) as days
--     from
--         daily_sales 
-- )

-- select
--     visited_on,
--     week_amount as amount,
--     round(week_amount / days, 2) as average_amount
-- from
--     moving_sales
-- -- where
-- --     visited_on >= date('2019-01-07');

WITH TEMP1 AS (
    SELECT visited_on, SUM(amount) amount 
    FROM Customer 
    GROUP BY visited_on 
    ORDER BY visited_on
),
TEMP2 AS(
SELECT visited_on,
SUM(amount) over(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount,
ROUND(AVG(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount,
ROW_NUMBER() OVER(ORDER BY visited_on) AS R1
FROM TEMP1)
SELECT visited_on, amount, average_amount
FROM TEMP2
WHERE R1>6;