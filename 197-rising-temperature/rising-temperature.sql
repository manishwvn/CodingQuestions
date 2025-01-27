select
    w1.id as Id
from
    Weather w1
left join
    Weather w2
on
    w2.recordDate = w1.recordDate - INTERVAL 1 DAY
where
    w1.temperature > w2.temperature;