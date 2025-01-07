select
distinct user_id
from
(select
user_id,
count(1)over(partition by user_id order by created_at range between interval 7 day preceding and current row) as rolling_cnt
from Users) as t1
where rolling_cnt > 1