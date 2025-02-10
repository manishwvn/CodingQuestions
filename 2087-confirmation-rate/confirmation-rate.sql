-- SELECT
--     S.USER_ID,
--     ROUND(AVG(CASE WHEN C.ACTION = 'confirmed' then 1 else 0 end), 2)
--         as confirmation_rate
-- FROM
--     SIGNUPS S
-- LEFT JOIN
--     CONFIRMATIONS C
-- ON
--     S.USER_ID = C.USER_ID
-- GROUP BY S.USER_ID;

select
    s.user_id,
    round(sum(case when c.action = 'confirmed' then 1 else 0 end) / count(*), 2)
    as confirmation_rate
from
    signups s
left join
    confirmations c
on
    s.user_id = c.user_id
group by
    s.user_id;