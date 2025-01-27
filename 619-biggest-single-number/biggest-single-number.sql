-- select case when count(*) > 0 then max(num)
--             else null
--             end as num from (select
--     num
-- from
--     MyNumbers
-- group by num
-- having count(num) = 1) as t;
with singlenums as (
    select
        num, count(*) as count
    from
        mynumbers
    group by
        num
    having count(*) = 1)

select
    max(num) as num
from
    singlenums;