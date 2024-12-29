select
    distinct user_id,
    count(1) as followers_count
from
    followers
group by
    user_id
order by 1;