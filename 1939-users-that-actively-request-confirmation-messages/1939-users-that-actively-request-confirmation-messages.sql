select
    distinct c.user_id
from 
    confirmations c
join
    confirmations c1
on
    c.user_id = c1.user_id
where
    c.time_stamp > c1.time_stamp
and
    timestampdiff(second, c1.time_stamp, c.time_stamp) <= (60 * 60 * 24);
    