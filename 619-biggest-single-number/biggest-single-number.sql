select case when count(*) > 0 then max(num)
            else null
            end as num from (select
    num
from
    MyNumbers
group by num
having count(num) = 1) as t;